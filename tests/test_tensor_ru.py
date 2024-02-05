import allure


def test_elements_display(sbis_page, tensor_page):
    sbis_page.click_on_contacts_btn()
    tensor_page.click_on_tensor_banner()

    assert tensor_page.check_switch_to_tensor_page()

    tensor_page.check_humans_power_block()
    tensor_page.click_on_more_details()
    assert tensor_page.check_switch_to_more_details_page()

    with allure.step('Checking what the photos have same height and width'):
        for image in tensor_page.find_images_in_working_block():
            height = image.get_attribute('height')
            width = image.get_attribute('width')
            assert height == width,\
                f'Высота изображения - {height} отличается от ширины изображения {width}'



