<template>
  <v-container class="text-center">
    <v-card elevation="2" tile max-width="500" class="ma-auto">
      <v-card-title>Profile</v-card-title>
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
          v-model="state.password"
          label="Password"
          :append-inner-icon="passwordShow ? 'mdi-eye' : 'mdi-eye-off'"
          :type="passwordShow ? 'text' : 'password'"
          @click:append-inner="passwordShow = !passwordShow"
          :error-messages="v$.password.$errors.map((e: any) => e.$message)"
          @input="v$.password.$touch"
          @blur="v$.password.$touch"
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
        <v-btn @click="submitForm">Update</v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import useValidate from "@vuelidate/core";
import { email, maxLength, minLength, required } from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import UpdateUser from "../models/user/update-user";
import UserDataService from "../services/UserDataService";

export default defineComponent({
  name: "Profile",
  setup() {
    const state = reactive({
      username: "",
      email: "",
      password: "",
      address: "",
      phone: "",
    });

    const rules = computed(() => {
      return {
        username: { required },
        email: { required, email },
        password: { required },
        address: { required },
        phone: {
          required,
          minLength: minLength(10),
          maxLength: maxLength(10),
        },
      };
    });

    const v$ = useValidate(rules, state);

    const user_id = Number(sessionStorage.getItem("user"));
    if (user_id) {
      UserDataService.get(user_id).then((response: any) => {
        state.username = response["data"]["username"];
        state.email = response["data"]["email"];
        state.password = response["data"]["password"];
        state.address = response["data"]["address"];
        state.phone = response["data"]["phone"];
      });
    }

    return { user_id, state, v$ };
  },
  data() {
    return {
      passwordShow: false,
    };
  },
  methods: {
    submitForm() {
      this.v$.$validate();
      if (!this.v$.$error) {
        const user: UpdateUser = {
          username: this.state.username,
          email: this.state.email,
          password: this.state.password,
          address: this.state.address,
          phone: this.state.phone,
        };
        // UserDataService.update(this.user_id, user)
        //   .then((response: any) => {
        //     console.log(response);
        //   })
        //   .catch((e: Error) => {
        //     console.log(e);
        //   });
      }
    },
  },
});
</script>
