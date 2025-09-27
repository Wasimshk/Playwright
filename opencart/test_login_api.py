from playwright.sync_api import Playwright


def test_loginapi(playwright:Playwright):
    context = playwright.request.new_context(base_url="https://www.opencart.com")
    context.post(url="/index.php?route=account/login", )

    response = context.post(
        url="/index.php?route=account/login",
        form={
            "email": "wasim.shaikh.allpro@gmail.com",
            "password": "Wasim@4210"
        }
    )

    print(response.status)
    print(response.text())