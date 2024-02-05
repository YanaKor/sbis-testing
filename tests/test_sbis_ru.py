import allure


def test_region_change(sbis_page):
    sbis_page.click_on_contacts_btn()

    with allure.step(''):
        assert sbis_page.checking_region_display() == 'г. Севастополь' and sbis_page.checking_partners_list()

    sbis_page.open_region_chooser()
    sbis_page.choose_kamchatka_krai()

    with allure.step(''):
        assert sbis_page.checking_region_display() == 'Камчатский край' \
               and sbis_page.check_switch_to_kamchatka_krai_page() \
               and sbis_page.checking_browser_tab_title() == 'СБИС Контакты — Камчатский край'
