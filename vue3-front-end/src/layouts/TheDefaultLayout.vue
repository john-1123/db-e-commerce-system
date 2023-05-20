<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
    name: "TheDefaultLayout",
});
</script>

<template>
    <v-layout>
        <v-app-bar color="grey-darken-2">
            <v-btn to="/home">
                <v-icon icon="mdi-home" start/>
                E-Commerce
            </v-btn>
            <v-btn to="/sign-in">SignIn</v-btn>
            <v-btn to="/sign-up">SignUp</v-btn>
            <v-btn to="/profile">Profile</v-btn>
            <v-btn to="/carts">Cart</v-btn>
            <v-btn to="/orders">Order</v-btn>
            <v-btn to="/manage/product">Manage Product</v-btn>
        </v-app-bar>
        <v-main>
            <slot></slot>
        </v-main>
    </v-layout>
</template>



