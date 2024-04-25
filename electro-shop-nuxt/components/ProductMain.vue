<template>
  <div class="product-details">
    <div class="product-images">
      <div class="main-image">
        <div class="image-container">
          <img
            src="/product-photo.png"
            alt="Apple iPhone 14 Pro main image"
            class="img-main"
          />
        </div>
        <div class="thumbnail-images">
          <div class="thumbnail">
            <div class="thumbnail-container">
              <img
                src="/product-photo.png"
                alt="Apple iPhone 14 Pro thumbnail 1"
                class="img-thumbnail"
              />
            </div>
          </div>
          <div class="thumbnail">
            <div class="thumbnail-container">
              <img
                src="/product-photo.png"
                alt="Apple iPhone 14 Pro thumbnail 2"
                class="img-thumbnail"
              />
            </div>
          </div>
          <div class="thumbnail">
            <div class="thumbnail-container">
              <img
                src="/product-photo.png"
                alt="Apple iPhone 14 Pro thumbnail 3"
                class="img-thumbnail"
              />
            </div>
          </div>
          <div class="thumbnail">
            <div class="thumbnail-container">
              <img
                src="/product-photo.png"
                alt="Apple iPhone 14 Pro thumbnail 4"
                class="img-thumbnail"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="product-info">
      <div class="info-container">
        <div class="title-stock">
          <h1 class="product-title">Apple iPhone 14 Pro</h1>
          <div class="stock-status">In Stock</div>
        </div>
        <div class="rating">
          <div>
            <b-icon icon="star-fill" class="star-icon"></b-icon>
            <b-icon icon="star-fill" class="star-icon"></b-icon>
            <b-icon icon="star-fill" class="star-icon"></b-icon>
            <b-icon icon="star-fill" class="star-icon"></b-icon>
            <b-icon icon="star-fill" class="star-icon"></b-icon>
          </div>
          <div class="rating-text">5.0 (121 Reviews)</div>
        </div>
        <div class="price">${{ product_pricing[selected_color] }}</div>
        <div class="description">
          It is a long established fact that a reader will be distracted by the
          readable content of a page when looking at its layout. The point of
          using Lorem Ipsum is that it has a more-or-less normal distribution.
        </div>
        <div class="color-label">Color</div>
        <div class="color-options">
          <div
            @click="selected_color = 'color_1'"
            class="color-option color1"
            :class="{ active: selected_color === 'color_1' }"
          ></div>
          <div
            @click="selected_color = 'color_2'"
            class="color-option color2"
            :class="{ active: selected_color === 'color_2' }"
          ></div>
          <div
            @click="selected_color = 'color_3'"
            class="color-option color3"
            :class="{ active: selected_color === 'color_3' }"
          ></div>
          <div
            @click="selected_color = 'color_4'"
            class="color-option color4"
            :class="{ active: selected_color === 'color_4' }"
          ></div>
        </div>
        <div class="add-to-cart">
          <div class="quantity">
            <b-icon icon="dash" font-scale="2" class="quantity-icon decrease" />
            <div class="quantity-value">1</div>
            <b-icon icon="plus" font-scale="2" class="quantity-icon increase" />
          </div>
          <div class="add-to-cart-btn">
            <button class="cart-button" @click="add_to_cart()">
              Add to Cart
            </button>
            <div class="wishlist-icon">
              <svg
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M12.765 4.70229L12 5.52422L11.235 4.70229C9.12233 2.43257 5.69709 2.43257 3.58447 4.70229C1.47184 6.972 1.47184 10.6519 3.58447 12.9217L10.4699 20.3191C11.315 21.227 12.685 21.227 13.5301 20.3191L20.4155 12.9217C22.5282 10.6519 22.5282 6.972 20.4155 4.70229C18.3029 2.43257 14.8777 2.43257 12.765 4.70229Z"
                  stroke="#101316"
                  stroke-width="1.5"
                  stroke-linejoin="round"
                />
              </svg>
            </div>
          </div>
        </div>
        <div class="share-label">Share</div>
        <div class="share-icons">
          <div class="share-icon">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M18 3H15C12.2386 3 10 5.23858 10 8V10H6V14H10V21H14V14H18V10H14V8C14 7.44772 14.4477 7 15 7H18V3Z"
                fill="#101316"
              />
            </svg>
          </div>
          <div class="share-icon">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M15.2859 4C13.1821 4 11.4766 5.79086 11.4766 8C11.4766 8.33382 11.5155 8.65809 11.5889 8.96808C9.56599 8.96808 6.51902 8.55908 3.97432 6.00961C3.63593 5.67059 3.01196 5.89726 3.03543 6.37567C3.41256 14.0627 6.70465 16.3049 8.39998 16.4444C7.30523 17.5257 5.71498 18.3791 4.11477 18.7622C3.69244 18.8633 3.58811 19.3256 4.00108 19.4599C5.14611 19.8323 6.78504 19.9758 7.66723 20C13.9081 20 18.9805 14.7471 19.0934 8.22229C19.9127 7.68945 20.4376 6.5325 20.7325 5.71291C20.8043 5.5133 20.4772 5.28073 20.2813 5.36226C19.6693 5.61708 18.8922 5.67749 18.2303 5.46181C17.5316 4.56927 16.4721 4 15.2859 4Z"
                fill="#101316"
              />
            </svg>
          </div>
          <div class="share-icon">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M7 2C4.23858 2 2 4.23858 2 7V17C2 19.7614 4.23858 22 7 22H17C19.7614 22 22 19.7614 22 17V7C22 4.23858 19.7614 2 17 2H7ZM18 7C18.5523 7 19 6.55228 19 6C19 5.44772 18.5523 5 18 5C17.4477 5 17 5.44772 17 6C17 6.55228 17.4477 7 18 7ZM17 12C17 14.7614 14.7614 17 12 17C9.23858 17 7 14.7614 7 12C7 9.23858 9.23858 7 12 7C14.7614 7 17 9.23858 17 12ZM12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z"
                fill="#101316"
              />
            </svg>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      product_pricing: {
        color_1: 100,
        color_2: 120,
        color_3: 130,
        color_4: 150,
      },
      selected_color: "color_1",
    };
  },
  methods: {
    add_to_cart() {
      const newProduct = {
        id: 3,
        product_name: "Apple iPhone 14 Pro Max",
        price: 1100,
        quantity: 1,
        image: "/product-photo.png"
      };
      this.$store.dispatch("add_to_cart", newProduct);
    },
  }
}
</script>

<style scoped>
.star-icon {
  color: #ffc11f;
}

.product-details {
  display: flex;
  gap: 20px;
}

@media (max-width: 991px) {
  .product-details {
    flex-direction: column;
    align-items: stretch;
    gap: 0;
  }
}

.product-images {
  width: 50%;
  margin-left: 0;
}

@media (max-width: 991px) {
  .product-images {
    width: 100%;
  }
}

.main-image {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

@media (max-width: 991px) {
  .main-image {
    max-width: 100%;
    margin-top: 30px;
  }
}

.image-container {
  background-color: var(--gray-gray-5, rgba(165, 169, 172, 0.05));
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 68px 60px;
}

@media (max-width: 991px) {
  .image-container {
    max-width: 100%;
    padding: 0 20px;
  }
}

.img-main {
  aspect-ratio: 0.83;
  object-fit: auto;
  object-position: center;
  width: 346px;
  max-width: 100%;
}

.thumbnail-images {
  margin-top: 20px;
  padding: 0 20px;
  display: flex;
  gap: 20px;
}

@media (max-width: 991px) {
  .thumbnail-images {
    max-width: 100%;
  }
}

.thumbnail {
  width: 25%;
}

@media (max-width: 991px) {
  .thumbnail {
    width: 100%;
  }
}

.thumbnail-container {
  background-color: var(--gray-gray-5, rgba(165, 169, 172, 0.05));
  display: flex;
  align-items: center;
  justify-content: center;
  width: 123px;
  height: 123px;
  margin: 0 auto;
  padding: 0 26px;
}

@media (max-width: 991px) {
  .thumbnail-container {
    margin-top: 20px;
    padding: 0 20px;
  }
}

.img-thumbnail {
  aspect-ratio: 0.83;
  object-fit: auto;
  object-position: center;
  width: 71px;
}

.product-info {
  width: 50%;
  margin-left: 20px;
}

@media (max-width: 991px) {
  .product-info {
    width: 100%;
  }
}

.info-container {
  display: flex;
  flex-direction: column;
  padding: 0 20px;
}

@media (max-width: 991px) {
  .info-container {
    max-width: 100%;
    margin-top: 30px;
  }
}

.title-stock {
  display: flex;
  gap: 20px;
}

@media (max-width: 991px) {
  .title-stock {
    max-width: 100%;
    flex-wrap: wrap;
  }
}

.product-title {
  color: var(--Dark-500, #101316);
  flex-grow: 1;
  flex-basis: auto;
  font: 700 30px/140% Montserrat, sans-serif;
}

.stock-status {
  justify-content: center;
  border-radius: 4px;
  background-color: rgba(60, 209, 57, 0.1);
  align-self: start;
  color: #3cd139;
  padding: 5px 10px;
  font: 400 12px/167% Montserrat, sans-serif;
}

.rating {
  align-self: start;
  display: flex;
  margin-top: 9px;
  gap: 8px;
  font-size: 16px;
  color: var(--Gray-500, #a5a9ac);
  font-weight: 400;
  line-height: 30px;
}

.rating-stars {
  aspect-ratio: 5;
  object-fit: auto;
  object-position: center;
  width: 120px;
  max-width: 100%;
  margin: auto 0;
}

.price {
  color: var(--Dark-500, #101316);
  margin-top: 18px;
  font: 400 20px/150% Montserrat, sans-serif;
}

@media (max-width: 991px) {
  .price {
    max-width: 100%;
  }
}

.description {
  color: var(--Dark-500, #101316);
  margin-top: 31px;
  font: 400 16px/30px Montserrat, sans-serif;
}

@media (max-width: 991px) {
  .description {
    max-width: 100%;
  }
}

.color-label {
  color: var(--Dark-500, #101316);
  align-self: start;
  margin-top: 26px;
  font: 700 18px/167% Montserrat, sans-serif;
}

.color-options {
  align-self: start;
  display: flex;
  margin-top: 14px;
  padding-right: 80px;
  gap: 10px;
}

@media (max-width: 991px) {
  .color-options {
    padding-right: 20px;
  }
}

.color-option {
  border-radius: 4px;
  width: 36px;
  height: 36px;
  cursor: pointer;
}

.color1 {
  background-color: #bebec6;
}

.color2 {
  background-color: var(--Color-Option-Color-Option-4, #304fbe);
}

.color3 {
  background-color: var(--Dark-500, #101316);
}

.color4 {
  background-color: var(--Color-Option-Color-Option-3, #5d30be);
}

.add-to-cart {
  display: flex;
  margin-top: 50px;
  gap: 20px;
}

@media (max-width: 991px) {
  .add-to-cart {
    flex-wrap: wrap;
    margin-top: 40px;
  }
}

.quantity {
  display: flex;
  gap: 0;
  font-size: 16px;
  color: var(--Dark-500, #101316);
  font-weight: 400;
  white-space: nowrap;
  text-align: center;
  line-height: 187.5%;
}

@media (max-width: 991px) {
  .quantity {
    white-space: initial;
  }
}

.quantity-icon {
  aspect-ratio: 0.71;
  object-fit: auto;
  object-position: center;
  width: 40px;
  border-color: rgba(165, 169, 172, 0.2);
  border-style: solid;
  border-width: 1px;
}

.decrease {
  border-radius: 10px 0 0 10px;
  height: 100%;
}

.quantity-value {
  border-color: rgba(165, 169, 172, 0.2);
  border-style: solid;
  border-top-width: 1px;
  border-bottom-width: 1px;
  width: 3rem;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (max-width: 991px) {
  .quantity-value {
    white-space: initial;
  }
}

.increase {
  border-radius: 0 10px 10px 0;
  height: 100%;
}

.add-to-cart-btn {
  display: flex;
  gap: 20px;
  flex-grow: 1;
  flex-basis: auto;
}

.cart-button {
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  background-color: var(--Primary-500, #1c4e8e);
  color: var(--White-500, #fff);
  flex-grow: 1;
  width: fit-content;
  padding: 13px 20px;
  font: 400 16px/30px Montserrat, sans-serif;
  border: none;
  cursor: pointer;
}

.wishlist-icon {
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  background-color: var(--gray-gray-5, rgba(165, 169, 172, 0.05));
  display: flex;
  width: 56px;
  height: 56px;
  padding: 0 16px;
}

.wishlist-img {
  aspect-ratio: 1;
  object-fit: auto;
  object-position: center;
  width: 24px;
}

.share-label {
  color: var(--Dark-500, #101316);
  margin-top: 30px;
  font: 700 18px/167% Montserrat, sans-serif;
}

@media (max-width: 991px) {
  .share-label {
    max-width: 100%;
  }
}

.share-icons {
  align-self: start;
  display: flex;
  margin-top: 8px;
  gap: 10px;
}

.share-icon {
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  border-color: rgba(165, 169, 172, 0.2);
  border-style: solid;
  border-width: 1px;
  display: flex;
  padding: 20px;
}

.share-img {
  aspect-ratio: 1;
  object-fit: auto;
  object-position: center;
  width: 24px;
}

.color-option.active {
  border: 2px solid;
}
</style>
