from racing.models import Accessory, ProductImage


def generate_product_response(product):
    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "is_active": product.is_active,
        "sale_status": product.sale_status,
        "description": product.description,
        "accessory_id": product.accessory_id,
        "created_time": product.created_time,
        "updated_time": product.updated_time
    }


def fill_accessory_info(product_response_list):
    accessory_ids = list(res["accessory_id"] for res in product_response_list)
    accessories = list(Accessory.objects.filter(id__in=accessory_ids))
    accessory_map = {acc.id: acc for acc in accessories}

    for p in product_response_list:
        p["accessory_name"] = accessory_map[p["id"]].name


def fill_image_info(product_response_list):
    product_ids = list(res["id"] for res in product_response_list)
    images = list(ProductImage.objects.filter(product_id__in=product_ids))

    image_map = {i.id: i for i in images}

    product_image_map = {}

    for i in images:
        if product_image_map.get(i.product_id):
            product_image_map[i.product_id] = []
        else:
            product_image_map[i.product_id].append(i.url)

    for res in product_response_list:
        res["urls"] = product_image_map.get(res["id"], [])
