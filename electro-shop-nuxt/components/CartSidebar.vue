<template>
  <b-sidebar id="cart-sidebar" title="Sidebar" right shadow>
    <div class="px-3 py-2">
      <main class="cart-items">
        <h2 class="cart-title">
          You have <span class="cart-count">{{ $store.state.products_in_cart.length }} items</span> in your cart
        </h2>
        <section v-for="(item, index) in $store.state.products_in_cart" :key="item.id" class="cart-item">
          <div class="item-details">
            <img
              src="/product-photo.png"
              alt="Apple iPhone 14 Pro"
              class="item-image"
            />
            <div class="item-info">
              <h3 class="item-name">{{ item.product_name }}</h3>
              <p class="item-price">${{ item.price }}</p>
              <p class="item-quantity">QTY: {{ item.quantity }}</p>
            </div>
          </div>
          <div @click="remove_from_cart(index)">
            <b-icon icon="trash-fill" variant="danger" class="item-remove" font-scale="2" />
          </div>
        </section>
      </main>
    </div>
  </b-sidebar>
</template>

<script>
export default {
    methods: {
        remove_from_cart(item_index) {
            this.$store.dispatch("remove_from_cart", item_index)
        }
    }
}
</script>
<style scoped>
.cart-items {
  display: flex;
  flex-direction: column;
  max-width: 312px;
  font-size: 14px;
  color: var(--Dark-500, #101316);
  font-weight: 400;
  line-height: 171%;
}

.cart-title {
  width: 100%;
  font: 16px/30px Montserrat, sans-serif;
}

.cart-count {
  font-weight: 700;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  width: 100%;
  gap: 20px;
  margin-top: 30px;
}

.item-details {
  display: flex;
  gap: 10px;
}

.item-image {
  width: 70px;
  aspect-ratio: 1;
  object-fit: cover;
  object-position: center;
}

.item-info {
  display: flex;
  flex-direction: column;
  padding: 0 20px;
  margin-top: 7px;
}

.item-name {
  font-family: Montserrat, sans-serif;
}

.item-price {
  font-family: Montserrat, sans-serif;
  font-weight: 700;
  margin-top: 11px;
}

.item-quantity {
  font-family: Montserrat, sans-serif;
  margin-top: 11px;
}

.item-remove {
  width: 20px;
  aspect-ratio: 1;
  object-fit: cover;
  object-position: center;
  align-self: end;
  margin-top: 50px;
  cursor: pointer;
}

.item-separator {
  width: 100%;
  min-height: 1px;
  background-color: var(--gray-gray-20, rgba(165, 169, 172, 0.2));
  margin-top: 20px;
}
</style>
