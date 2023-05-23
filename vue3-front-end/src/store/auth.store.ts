import { createStore } from "vuex";

export const authStore = createStore({
  state() {
    return {
      isLogin: false,
    };
  },

  mutations: {
    login(state) {
      state.isLogin = true;
    },
    logout(state) {
      state.isLogin = false;
    },
  },
});
