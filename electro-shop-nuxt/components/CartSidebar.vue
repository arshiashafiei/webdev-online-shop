<template>
  <b-sidebar id="cart-sidebar" title="Sidebar" right shadow no-header bg-variant="white">
    <div class="px-3 py-2">
      <main class="cart-items">
        <h2 class="cart-title">
          You have <span class="cart-count">{{ $store.state.products_in_cart.length }} items</span> in your cart
        </h2>
        <div v-for="(item, index) in $store.state.products_in_cart" :key="item.id">
          <section class="cart-item">
          <div class="item-details">
            <b-img fluid
              :src="item.image"
              alt="Apple iPhone 14 Pro"
              class="item-image"
            />
            <div class="item-info">
              <p class="item-name mb-1">{{ item.product_name }}</p>
              <p class="item-price mb-1">${{ item.price }}</p>
              <p class="item-quantity mb-1">QTY: {{ item.quantity }}</p>
            </div>
          </div>
          <div class="align-self-end" @click="remove_from_cart(index)">
            <b-icon icon="trash" variant="danger" class="item-remove" font-scale="3" />
          </div>
          
        </section>

          <div class="separator mt-3"></div>
        </div>
        
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
.separator {
  border: 1px solid rgba(165, 169, 172, 0.2);
}

.cart-items {
  display: flex;
  flex-direction: column;
  color: #101316;
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
  margin-top: 30px;
}

.item-details {
  display: flex;
  gap: 10px;
}

.item-image {
  align-self: center;
  width: 70px;
}

.item-info {
  display: flex;
  flex-direction: column;
  padding: 0 20px;
}

.item-price {
  font-weight: 700;
}

.item-remove {
  width: 20px;
  align-self: end;
  cursor: pointer;
}

.item-separator {
  width: 100%;
  min-height: 1px;
  background-color: var(--gray-gray-20, rgba(165, 169, 172, 0.2));
  margin-top: 20px;
}
</style>
