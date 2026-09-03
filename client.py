class AutonomousStorefrontCartActionPlannerClient:
    def plan_storefront_cart_actions(self, target_storefront_url='https://shop.brand.com/products/4k-drone', target_sku='DRN-4K-BLK', user_spending_limit_usd=799.00):
        return {
            'cart_plan_id': 'crt_pln_9918',
            'storefront_url': target_storefront_url,
            'planned_action_steps': [
                {'action': 'CLICK', 'target': 'select#color-black', 'description': 'Select Black colorway'},
                {'action': 'CLICK', 'target': 'button#add-to-cart', 'description': 'Add SKU to basket'},
                {'action': 'NAVIGATE', 'target': '/checkout', 'description': 'Proceed to secure checkout'}
            ],
            'human_in_the_loop_approval_required': True,
            'cart_action_manifest_url': 'https://commerce.agent.genpark.ai/plans/9918.json'
        }
