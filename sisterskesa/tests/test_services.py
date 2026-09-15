import unittest
from decimal import Decimal
from data.products import PRODUCTS
from services.cart_service import add_item, set_quantity, totals, unit_price
from services.checkout_service import place_demo_order
from services.filter_service import filter_products, sort_products
from services.search_service import search_products
from services.media_service import get_media, ROOT
from data.media_manifest import MEDIA

class ShoppingTests(unittest.TestCase):
    def setUp(self):
        self.cart = {}
        self.p = PRODUCTS[0]
    def test_catalogue(self):
        self.assertEqual(len(PRODUCTS),21)
        self.assertEqual(len({p.slug for p in PRODUCTS}),21)
        self.assertEqual(len({p.category for p in PRODUCTS}),4)
        self.assertTrue(all(p.brand == "SISTERSKESA" for p in PRODUCTS))
        self.assertEqual(sum(p.featured for p in PRODUCTS),8)
    def test_rounding_and_size(self):
        self.assertEqual(unit_price(self.p,'50 g',True), Decimal('35.28'))
        self.assertEqual(unit_price(self.p,'30 g'), Decimal('26.98'))
        self.assertEqual(unit_price(self.p,'30 g',True), Decimal('22.93'))
    def test_variant_identity(self):
        a=add_item(self.cart,self.p,'50 g')
        add_item(self.cart,self.p,'50 g')
        add_item(self.cart,self.p,'30 g')
        add_item(self.cart,self.p,'50 g',True,'Every 6 weeks')
        self.assertEqual(len(self.cart),3)
        self.assertEqual(self.cart[a]['quantity'],2)
    def test_shipping_threshold(self):
        key=add_item(self.cart,self.p,'50 g',quantity=2)
        self.assertEqual(totals(self.cart)['remaining'],Decimal('2.00'))
        self.assertEqual(totals(self.cart)['total'],Decimal('89.00'))
        set_quantity(self.cart,key,3)
        self.assertEqual(totals(self.cart)['shipping'],0)
    def test_savings(self):
        add_item(self.cart,self.p,'50 g',True)
        self.assertEqual(totals(self.cart)['savings'],Decimal('6.22'))
        self.assertEqual(totals({})['total'],0)
    def test_validation(self):
        with self.assertRaises(ValueError): add_item(self.cart,self.p,'invalid')
        with self.assertRaises(ValueError): add_item(self.cart,next(p for p in PRODUCTS if p.id == "p014"),"100 ml")
        with self.assertRaises(ValueError): add_item(self.cart,self.p,'50 g',quantity=21)
        with self.assertRaises(ValueError): add_item(self.cart,self.p,'50 g',True,'Never')
    def test_filters(self):
        result=filter_products(PRODUCTS,{'texture':['Oil'],'care_goals':['Face Ritual']},'skincare')
        self.assertEqual([p.name for p in result],['Hibiscus Face Oil', 'Rosehip & Sesame Face Oil'])
        self.assertFalse(filter_products(PRODUCTS,{'price':(100,320)}))
        self.assertTrue(all(p.availability!='Out of Stock' for p in filter_products(PRODUCTS,{'availability':['In Stock']})))
        self.assertTrue(all(p.new_arrival for p in filter_products(PRODUCTS,{},new_only=True)))
    def test_search(self):
        self.assertEqual(search_products(PRODUCTS,'KASTURI TURMERIC')[0].id,'p001')
        self.assertTrue(search_products(PRODUCTS,'body ritual'))
        self.assertFalse(search_products(PRODUCTS,'zzzz'))
    def test_sort(self):
        result=sort_products(list(PRODUCTS),'Price: low to high')
        values=[p.sale_price if p.sale_price is not None else p.price for p in result]
        self.assertEqual(values,sorted(values))
    def test_checkout(self):
        add_item(self.cart,self.p,'50 g')
        details={'email':'demo@example.com','name':'Demo Guest','address':'10 Example Lane','city':'Example City','postal':'10001','country':'United States'}
        order=place_demo_order(self.cart,details,True)
        self.assertTrue(order['demo'])
        self.assertEqual(order['totals']['total'],'47.50')
        self.cart.clear()
        self.assertTrue(order['items'])
        with self.assertRaises(ValueError): place_demo_order({},details,True)
        with self.assertRaises(ValueError): place_demo_order(order['items'],details,False)
    def test_local_media(self):
        for key,entry in MEDIA.items():
            self.assertTrue((ROOT/entry['local_path']).is_file(),key)
            self.assertTrue(get_media(key).startswith('data:image/webp;base64,'),key)

if __name__=='__main__': unittest.main()
