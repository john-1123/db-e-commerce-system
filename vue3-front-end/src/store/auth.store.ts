import { createStore } from "vuex";
import User from "../models/user/user";

export const authStore = createStore({
  state() {
    return {
      isLogin: sessionStorage.getItem("user") != undefined ? true : false,
    };
  },

  mutations: {
    login(state, user: User) {
      state.isLogin = true;
      sessionStorage.setItem("user", user.user_id!.toString());
    },
    logout(state) {
      state.isLogin = false;
      sessionStorage.clear();
    },
  },
});
