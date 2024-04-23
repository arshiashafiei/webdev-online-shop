<template>
  <b-container class="my-5">
    <b-row class="mb-3">
      <b-col>
        <h2 class="title">Top Selling Products</h2>
      </b-col>
      <b-col>
        <b-nav align="right" class="nav">
          <b-nav-item class="active">
            <div class="d-flex flex-column">
              New
              <span class="underline"></span>
            </div>
          </b-nav-item>
          <b-nav-item disabled>Featured</b-nav-item>
          <b-nav-item disabled>Top Rated</b-nav-item>
        </b-nav>
      </b-col>
    </b-row>

    <b-row>
      <b-col cols="12" lg="4">
        <div class="d-flex flex-column">
          <div class="gray-background pl-3 pt-3">
            <h1 class="product-name">Apple iPad Pro Wi-Fi</h1>
            <h2 class="product-price">$1520</h2>
            <div class="d-flex justify-content-end">
              <b-img
                src="/images/iphone-main.png"
                alt="Apple iPad Pro Wi-Fi"
              />
            </div>
          </div>
        </div>
      </b-col>

      <b-col cols="12" lg="8">
        <b-row>
          <b-col cols="12" md="6" lg="4" v-for="item in items" :key="item">
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
          image: "/top-seller/1.png",
          name: "Panasonic Lumix DC-GH5 II",
          price: "1500.00",
        },
        {
          image: "/top-seller/2.png",
          name: "Asus ROG Delta S",
          price: "250.00",
        },
        {
          image: "/top-seller/3.png",
          name: "Xiaomi Fimi X8 Mini",
          price: "650.00",
        },
        {
          image: "/top-seller/4.png",
          name: "Apple iPhone 13",
          price: "500.00",
        },
        {
          image: "/top-seller/5.png",
          name: "Fossil Gen 6 Smart Watch",
          price: "450.00",
        },
        {
          image: "/top-seller/6.png",
          name: "Apple iPad Air Wi-Fi",
          price: "850.00",
        },
      ],
    };
  },
};
</script>

<style scoped>
.star-icon {
  color: #ffc11f;
}

.product-name {
  font-family: Montserrat, sans-serif;
  font-weight: 700;
  line-height: 42px;
  width: 310px;
  margin-top: 12px;
}

.product-price {
  font-family: Montserrat, sans-serif;
  font-weight: 400;
  line-height: 140%;
}

@media (max-width: 991px) {
  .product-price {
    margin-bottom: 40px;
  }
}

.active {
  color: #1c4e8e;
}

.underline {
  height: 1px;
  background-color: #1c4e8e;
}

.nav {
  font-size: 20px;
  font-weight: 400;
  line-height: 150%;
}

.title {
  font: 700 30px/140% Montserrat, sans-serif;
}
</style>
