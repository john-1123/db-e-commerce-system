import { createStore } from "vuex";
import User from "../models/user/user";

export const authStore = createStore({
  state() {
    return {
      isLogin: false,
    };
  },

  mutations: {
    login(state, user: User) {
      state.isLogin = true;
      localStorage.setItem('user', user.username);
    },
    logout(state) {
      state.isLogin = false;
      localStorage.clear();
    },
  },
});
