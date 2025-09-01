curl --location 'https://yourdomain.myshoplaza.com/openapi/2022-01/products' \
--header 'access-token:token ' \
--header 'Content-Type: application/json' \
--data '{
  "product": {
    "title": "Multi-Variant Product Example",
    "brief": "A brief description of the multi-variant product",
    "description": "Detailed description of this product with multiple variants",
    "published": true,
    "requires_shipping": true,
    "taxable": true,
    "tags": "t-shirt,summer,collection",
    "vendor": "Fashion Brand",
    "vendor_url": "https://example.com",
    "seo_title": "Premium Multi-Variant T-Shirt",
    "seo_description": "High quality t-shirt available in multiple colors and sizes",
    "seo_keywords": "t-shirt,cotton,summer",
    "handle": "multi-variant-tshirt",
    "has_only_default_variant": false,
    "inventory_tracking": true,
    "inventory_policy": "deny",
    "need_variant_image": true,
    "spu": "PROD12345",
    "fake_sales": 100,
    "display_fake_sales": true,
    "options": [
      {
        "name": "Color",
        "values": ["Red", "Blue", "Black"]
      },
      {
        "name": "Size",
        "values": ["S", "M", "L", "XL"]
      }
    ],
    "images": [
      {
        "src": "//cdn.shoplazza.com/free/5d4c48f9e65ffab9e73efbf1fd37a0f3.jpg",
        "width": 800,
        "height": 800,
        "alt": "Main product image"
      },
      {
        "src": "//cdn.shoplazza.com/free/5d4c48f9e65ffab9e73efbf1fd37a0f3.jpg",
        "width": 800,
        "height": 800,
        "alt": "Alternative product view"
      }
    ],
    "variants": [
      {
        "option1": "Red",
        "option2": "S",
        "image": {
          "src": "//cdn.shoplazza.com/free/5d4c48f9e65ffab9e73efbf1fd37a0f3.jpg"
        },
        "compare_at_price": "39.99",
        "price": "29.99",
        "sku": "TSHIRT-RED-S",
        "barcode": "123456789012",
        "inventory_quantity": 50,
        "weight": "0.2",
        "weight_unit": "kg",
        "cost_price": "15.00",
        "wholesale_price": [
          {
            "price": "25.00",
            "min_quantity": 10
          }
        ]
      },
      {
        "option1": "Red",
        "option2": "M",
        "image": {
          "src": "//cdn.shoplazza.com/free/5d4c48f9e65ffab9e73efbf1fd37a0f3.jpg"
        },
        "compare_at_price": "39.99",
        "price": "29.99",
        "sku": "TSHIRT-RED-M",
        "barcode": "123456789013",
        "inventory_quantity": 75,
        "weight": "0.22",
        "weight_unit": "kg",
        "cost_price": "15.00",
        "wholesale_price": [
          {
            "price": "25.00",
            "min_quantity": 10
          }
        ]
      },
      {
        "option1": "Blue",
        "option2": "L",
        "image": {
          "src": "//cdn.shoplazza.com/free/5d4c48f9e65ffab9e73efbf1fd37a0f3.jpg"
        },
        "compare_at_price": "39.99",
        "price": "29.99",
        "sku": "TSHIRT-BLUE-L",
        "barcode": "123456789014",
        "inventory_quantity": 60,
        "weight": "0.23",
        "weight_unit": "kg",
        "cost_price": "15.00",
        "wholesale_price": [
          {
            "price": "25.00",
            "min_quantity": 10
          }
        ]
      },
      {
        "option1": "Black",
        "option2": "XL",
        "image": {
          "src": "//cdn.shoplazza.com/free/5d4c48f9e65ffab9e73efbf1fd37a0f3.jpg"
        },
        "compare_at_price": "39.99",
        "price": "29.99",
        "sku": "TSHIRT-BLACK-XL",
        "barcode": "123456789015",
        "inventory_quantity": 40,
        "weight": "0.25",
        "weight_unit": "kg",
        "cost_price": "15.00",
        "wholesale_price": [
          {
            "price": "25.00",
            "min_quantity": 10
          }
        ]
      }
    ]
  }
