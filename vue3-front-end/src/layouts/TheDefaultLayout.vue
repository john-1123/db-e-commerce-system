<script lang="ts">
import { defineComponent } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

export default defineComponent({
  name: "TheDefaultLayout",
  setup() {
    const router = useRouter();
    const authStore = useStore();
    return { router, authStore };
  },
  methods: {
    Logout() {
      this.authStore.commit("logout");
      this.router.push("/home");
    },
  },
});
</script>

<template>
  <v-layout>
    <v-app-bar color="grey-darken-2">
      <v-btn to="/home">
        <v-icon icon="mdi-home" start />
        E-Commerce
      </v-btn>
      <v-btn to="/sign-in" v-if="!authStore.state.isLogin">SignIn</v-btn>
      <v-btn to="/sign-up" v-if="!authStore.state.isLogin">SignUp</v-btn>
      <v-btn to="/profile" v-if="authStore.state.isLogin">Profile</v-btn>
      <v-btn to="/carts" v-if="authStore.state.isLogin">Cart</v-btn>
      <v-btn to="/orders" v-if="authStore.state.isLogin">Order</v-btn>
      <v-btn v-if="authStore.state.isLogin" @click="Logout">Logout</v-btn>
    </v-app-bar>
    <v-main>
      <slot></slot>
    </v-main>
  </v-layout>
</template>
