<template>
  <v-container class="text-center">
    <v-btn to="/home" class="ma-5" color="warning">Go To Home</v-btn>
    <v-btn to="/sign-up" class="ma-5" color="success">Go To SignUp</v-btn>
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
</template>
<script lang="ts">
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "sign-up",
  setup() {
    const router = useRouter();

    const state = reactive({
      email: "",
      password: "",
    });

    const rules = computed(() => {
      return {
        email: { required },
        password: { required },
      };
    });

    const v$ = useValidate(rules, state);

    return { router, state, v$ };
  },
  data() {
    return {
      passwordShow: false,
    };
  },
  methods: {
    submitForm() {
      this.v$.$validate();
      if(!this.v$.$error) {
        // pass
        this.router.push('/home')
      }
    },
  },
});
</script>
