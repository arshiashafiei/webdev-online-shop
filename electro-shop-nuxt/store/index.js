export const state = () => {
    return ({
        products_in_cart: [
            {
                id: 1,
                product_name: "Apple iPhone 14 Pro",
                price: 100,
                quantity: 1,
                image: "/top-seller/4.png"
            },
            {
                id: 2,
                product_name: "Asus ROG Delta S",
                price: 150,
                quantity: 1,
                image: "/top-seller/2.png"
            },
        ],
        isAuthenticated: false,
        username: null

    });
};

export const actions = {
    add_to_cart({ commit }, payload) {
        commit('setProductsCart', payload);
    },
    remove_from_cart({ commit }, payload) {
        commit('removeProductsCart', payload);
    },
    async checkAuth({ commit }) {
        try {
          const response = await this.$axios.$get('/api/check-auth/');
          commit('setAuthUser', { isAuthenticated: true, username: response.username });
        } catch (error) {
          commit('setAuthUser', { isAuthenticated: false, username: null });
        }
      }
};

export const mutations = {
    setProductsCart(state, product) {
        state.products_in_cart.push(product);
    },
    removeProductsCart(state, product_index) {
        state.products_in_cart.splice(product_index, 1);
    },
    setAuthUser(state, { isAuthenticated, username }) {
        console.log(isAuthenticated);
        state.isAuthenticated = isAuthenticated;
        state.username = username;
      }
};
