# здесь хранятся константы паука apteka

START_URL = 'https://apteka-ot-sklada.ru'
ID_CITY = {'id': 92}
POST_CITY_URL = 'https://apteka-ot-sklada.ru/api/user/city/requestById'
HEADERS = {'Content-Type': 'application/json'}
CSS_CARD_URL = 'a.goods-card__link::attr(href)'
CSS_NEX_PAGE = 'li.ui-pagination__item.ui-pagination__item_next a::attr(href)'
CSS_PRODUCT_NAME = 'h1.text.text_size_display-1.text_weight_bold span::text'
CSS_MARKETING_TAGS = 'span.ui-tag.text.text_weight_medium.ui-tag_theme_secondary::text'
CSS_BRAND = 'span[itemtype="legalName"]::text'
CSS_PATH_CATEGORY = 'span.ui-link__text span[itemprop="name"]::text'
CSS_ORIGINAL_PRICE = 'meta[itemprop=price]::attr(content)'
CSS_IN_STOCK = 'li.goods-offer-panel__records-item span::text'
CSS_LIST_IMAGES = 'ul.goods-gallery__preview-list img::attr(src)'
CSS_METADATA = 'div.ui-collapsed-content__content'
CSS_COUNTRY = 'span[itemtype="location"]::text'