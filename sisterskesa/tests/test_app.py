import unittest
from streamlit.testing.v1 import AppTest

class AppTests(unittest.TestCase):
    def app(self,route='home'):
        at=AppTest.from_file('app.py',default_timeout=30)
        at.query_params['view']=route
        at.run()
        self.assertFalse(at.exception,[e.message for e in at.exception])
        return at
    def test_routes(self):
        for route in ('home','shop','category/skincare','category/hair-care','category/body-rituals','category/wellness','about','journal','journal/the-morning-shelf','cart','checkout','search','help/faq','help/privacy','product/manjal-rose-face-powder','product/bhringraj-amla-scalp-oil','missing'):
            with self.subTest(route=route): self.app(route)
    def test_cart_navigation_and_checkout(self):
        at=self.app('product/manjal-rose-face-powder')
        at.radio(key='size_p001').set_value('30 g').run()
        at.radio(key='mode_p001').set_value('Subscribe & save 15%').run()
        at.selectbox(key='cadence_p001').set_value('Every 6 weeks').run()
        at.button(key='add_to_bag').click().run()
        self.assertFalse(at.exception)
        self.assertEqual(len(at.session_state['cart']),1)
        at.button(key='nav_cart').click().run()
        self.assertEqual(at.query_params['view'],['cart'])
        at.number_input[0].set_value(2).run()
        self.assertEqual(next(iter(at.session_state['cart'].values()))['quantity'],2)
        at.button(key='checkout_button').click().run()
        # Invalid form stays in checkout with a visible error.
        at.button(key='FormSubmitter:checkout_form-PLACE DEMO ORDER  ↗').click().run()
        self.assertTrue(at.error)
        for field,value in zip(at.text_input,['demo@example.com','Demo Guest','10 Example Lane','Example City','10001']): field.set_value(value)
        at.checkbox[0].check()
        at.button(key='FormSubmitter:checkout_form-PLACE DEMO ORDER  ↗').click().run()
        self.assertFalse(at.exception,[e.message for e in at.exception])
        self.assertFalse(at.session_state['cart'])
        self.assertEqual(at.session_state['order']['totals']['subtotal'],'45.86')
    def test_filter_dialog(self):
        # AppTest does not emulate fragment reruns; invoke the dialog directly.
        at=AppTest.from_string("from utils.session import initialize; initialize(); from components.filters import filter_drawer; filter_drawer('all')",default_timeout=30).run()
        at.multiselect(key='filter_0_texture').set_value(['Oil']).run()
        next(b for b in at.button if b.label.startswith('SHOW RESULTS')).click().run()
        self.assertFalse(at.exception)
        self.assertEqual(at.session_state['filters']['texture'],['Oil'])
    def test_newsletter(self):
        at=self.app()
        at.text_input[0].set_value('bad-email')
        at.button(key='FormSubmitter:newsletter_form-JOIN THE LIST  ↗').click().run()
        self.assertTrue(at.error)
        at.text_input[0].set_value('demo@example.com')
        at.checkbox[0].check()
        at.button(key='FormSubmitter:newsletter_form-JOIN THE LIST  ↗').click().run()
        self.assertTrue(at.success)
        self.assertEqual(at.session_state['newsletter_emails'],['demo@example.com'])

if __name__=='__main__': unittest.main()
