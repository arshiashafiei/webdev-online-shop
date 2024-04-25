<template>
    <b-container class="p-0 mb-3">
        <b-row class="mt-3">
            <b-col cols="12" md="6" lg="3" v-for="item in items" :key="item">
                <div class="d-flex flex-column mb-4">
                    <div class="gray-background d-flex justify-content-center">
                        <b-img fluid :src="item.image" alt="Product image" />
                    </div>
                </div>
                <div class="product-name">{{ item.name }}</div>
                <div>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                    <b-icon icon="star-fill" class="star-icon"></b-icon>
                </div>
                <div class="product-price mb-3">${{ item.price }}</div>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
export default {
    data() {
        return {
            items: [
                {
                    image: "/images/apple-iphone.png",
                    name: "Apple iPhone 14 Plus",
                    price: "850.00",
                },
                {
                    image: "/top-seller/3.png",
                    name: "Xiaomi Fimi X8 Mini",
                    price: "650.00",
                },
                {
                    image: "/images/apple-ipad-mini.png",
                    name: "Apple iPad Mini 6 Wi-Fi",
                    price: "500.00",
                },
                {
                    image: "/top-seller/2.png",
                    name: "Asus ROG Delta S",
                    price: "250.00",
                }
            ]
        }
    }
}
</script>

<style scoped>
.star-icon {
    color: #ffc11f;
}

.product-name {
    font-weight: 700;
    line-height: 42px;
    width: 310px;
    margin-top: 12px;
}

.product-price {
    font-weight: 400;
    line-height: 140%;
}

@media (max-width: 991px) {
    .product-price {
        margin-bottom: 40px;
    }
}
</style>