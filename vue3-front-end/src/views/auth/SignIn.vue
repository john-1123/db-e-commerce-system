<template>
  <v-container class="text-center">
    <v-card elevation="2" tile max-width="500" class="ma-auto">
      <v-card-title>Sign In</v-card-title>
      <v-form class="ma-3">
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
        <v-btn @click="submitForm">SignIn</v-btn>
      </v-form>
    </v-card>
  </v-container>

  <v-dialog v-model="alertDialog" max-width="500">
    <v-card>
      <v-card-title> 提示訊息 </v-card-title>
      <v-card-text>
        {{ message }}
      </v-card-text>
      <v-card-actions class="justify-end">
        <v-btn class="mx-3" variant="tonal" @click="alertDialog = false"
          >關閉</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script lang="ts">
import useValidate from "@vuelidate/core";
import { required, email } from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import { useRouter } from "vue-router";

import { useStore } from "vuex";
import Login from "../../models/user/login";
import AuthService from "../../services/AuthService";

export default defineComponent({
  name: "sign-up",
  setup() {
    const router = useRouter();
    const authStore = useStore();
    const state = reactive({
      email: "",
      password: "",
    });

    const rules = computed(() => {
      return {
        email: { required, email },
        password: { required },
      };
    });

    const v$ = useValidate(rules, state);

    return { router, state, v$, authStore };
  },
  data() {
    return {
      passwordShow: false,
      alertDialog: false,
      message: "",
    };
  },
  methods: {
    submitForm() {
      this.v$.$validate();
      if (!this.v$.$error) {
        const user: Login = {
          email: this.state.email,
          password: this.state.password,
        };
        AuthService.login(user)
          .then((response: any) => {
            console.log(response);
            this.authStore.commit("login", response["data"]);
            this.router.push("/home");
          })
          .catch((e: Error) => {
            this.message = "請確認帳號密碼輸入正確!";
            this.alertDialog = true;
            console.log(e);
          });
      }
    },
  },
});
</script>
