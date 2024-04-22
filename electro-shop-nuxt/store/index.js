export const state = () => {
    return ({
        products_in_cart: [
            {
                id: 1,
                product_name: "Apple iPhone 14 Pro",
                price: 100,
                quantity: 1
            },
            {
                id: 2,
                product_name: "Asus ROG Delta S",
                price: 150,
                quantity: 1
            },
        ],

    });
};

export const actions = {
    add_to_cart({ commit }, payload) {
        commit('setProductsCart', payload);
    },
    remove_from_cart({ commit }, payload) {
        commit('removeProductsCart', payload);
    },
};

export const mutations = {
    setProductsCart(state, product) {
        state.products_in_cart.push(product);
    },
    removeProductsCart(state, product_index) {
        state.products_in_cart.splice(product_index, 1);
    },
};
