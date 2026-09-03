from client import AutonomousStorefrontCartActionPlannerClient

def main():
    client = AutonomousStorefrontCartActionPlannerClient()
    res = client.plan_storefront_cart_actions('https://store.acme.com/item/1', 'SKU-01', 150.0)
    print('Storefront Cart Action Planner: ' + res['cart_plan_id'])
    print('Action Steps: ' + str(len(res['planned_action_steps'])) + ' steps planned | HITL Approval: ' + str(res['human_in_the_loop_approval_required']))
    print('Manifest URL: ' + res['cart_action_manifest_url'])

if __name__ == '__main__':
    main()
