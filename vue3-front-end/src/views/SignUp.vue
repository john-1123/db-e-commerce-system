<template>
  <v-container class="text-center">
    <v-btn to="/home" class="ma-5" color="warning">Go To Home</v-btn>
    <v-card elevation="2" tile max-width="500" class="ma-auto">
      <v-card-title>Sign Up</v-card-title>
      <v-form class="ma-3">
        <v-text-field
          class="ma-3"
          v-model="state.username"
          label="Username"
          :error-messages="v$.username.$errors.map((e: any) => e.$message)"
          @input="v$.username.$touch"
          @blur="v$.username.$touch"
        ></v-text-field>
        <v-text-field
          class="ma-3"
          v-model="state.email"
          label="Email"
          :error-messages="v$.email.$errors.map((e: any) => e.$message)"
          @input="v$.email.$touch"
          @blur="v$.email.$touch"
        ></v-text-field>
        <v-text-field
          class="ma-3"
          v-model="state.password.password"
          label="Password"
          :append-inner-icon="passwordShow ? 'mdi-eye' : 'mdi-eye-off'"
          :type="passwordShow ? 'text' : 'password'"
          @click:append-inner="passwordShow = !passwordShow"
          :error-messages="v$.password.password.$errors.map((e: any) => e.$message)"
          @input="v$.password.password.$touch"
          @blur="v$.password.password.$touch"
        ></v-text-field>
        <v-text-field
          class="ma-3"
          v-model="state.password.confirm"
          label="Confirm Password"
          :append-inner-icon="confirmShow ? 'mdi-eye' : 'mdi-eye-off'"
          :type="confirmShow ? 'text' : 'password'"
          @click:append-inner="confirmShow = !confirmShow"
          :error-messages="v$.password.confirm.$errors.map((e: any) => e.$message)"
          @input="v$.password.confirm.$touch"
          @blur="v$.password.confirm.$touch"
        ></v-text-field>
        <v-text-field
          class="ma-3"
          v-model="state.address"
          label="Address"
          :error-messages="v$.address.$errors.map((e: any) => e.$message)"
          @input="v$.address.$touch"
          @blur="v$.address.$touch"
        ></v-text-field>
        <v-text-field
          class="ma-3"
          v-model="state.phone"
          label="Phone"
          :error-messages="v$.phone.$errors.map((e: any) => e.$message)"
          @input="v$.phone.$touch"
          @blur="v$.phone.$touch"
        ></v-text-field>
        <v-btn @click="submitForm">SignUp</v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>
<script lang="ts">
import useValidate from "@vuelidate/core";
import {
  email,
  maxLength,
  minLength,
  required,
  sameAs,
} from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import { useRouter } from "vue-router";
import CreateUser from "../models/user/create-user";
import UserDataService from "../services/UserDataService";

export default defineComponent({
  name: "sign-up",
  setup() {
    const router = useRouter();

    const state = reactive({
      username: "",
      email: "",
      password: {
        password: "",
        confirm: "",
      },
      address: "",
      phone: "",
    });

    const rules = computed(() => {
      return {
        username: { required },
        email: { required, email },
        password: {
          password: { required, minLength: minLength(6) },
          confirm: { required, sameAs: sameAs(state.password.password) },
        },
        address: { required },
        phone: { required, minLength: minLength(10), maxLength: maxLength(10) },
      };
    });

    const v$ = useValidate(rules, state);

    return { router, state, v$ };
  },
  data() {
    return {
      passwordShow: false,
      confirmShow: false,
    };
  },
  methods: {
    submitForm() {
      this.v$.$validate();
      if (!this.v$.$error) {
        const user: CreateUser = {
          username: this.state.username,
          email: this.state.email,
          password: this.state.password.password,
          address: this.state.address,
          phone: this.state.phone,
        };
        UserDataService.create(user).then((response: any) => {
          console.log(response);
          this.router.push('/sign-in');
        }).catch((e: Error) => {
          console.log(e);
        });
      }
    },
  },
});
</script>
