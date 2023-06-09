<template>
  <v-container class="text-center">
    <v-card elevation="2" tile max-width="500" class="ma-auto">
      <v-card-title>個人資料</v-card-title>
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
        <v-btn class="mx-3" color="blue" @click="submitForm">Update</v-btn>
        <v-btn class="mx-3" color="red" @click="openAlert()">註銷帳號</v-btn>
      </v-form>
    </v-card>

    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title> 提示訊息 </v-card-title>
        <v-card-text>
          {{ message }}
        </v-card-text>
        <v-card-actions>
          <v-row class="justify-end">
            <v-btn class="mx-3" variant="tonal" @click="close">關閉</v-btn>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="alertDialog" max-width="500">
      <v-card>
        <v-card-title> 提示訊息 </v-card-title>
        <v-card-text>
          {{ message }}
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn color="blue" variant="tonal" @click="deleteAccount"
            >確定</v-btn
          >
          <v-btn class="mx-3" variant="tonal" @click="close">關閉</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import useValidate from "@vuelidate/core";
import { email, maxLength, minLength, required } from "@vuelidate/validators";
import { computed, defineComponent, reactive } from "vue";
import UpdateUser from "../models/user/update-user";
import UserDataService from "../services/UserDataService";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

export default defineComponent({
  name: "Profile",
  setup() {
    const authStore = useStore();

    const router = useRouter();

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
      UserDataService.get(user_id)
        .then((response: any) => {
          state.username = response["data"]["username"];
          state.email = response["data"]["email"];
          state.password = response["data"]["password"];
          state.address = response["data"]["address"];
          state.phone = response["data"]["phone"];
        })
        .catch((e: Error) => {
          console.log(e);
        });
    }

    return { authStore, router, user_id, state, v$ };
  },
  data() {
    return {
      passwordShow: false,
      dialog: false,
      message: "",
      alertDialog: false,
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
        UserDataService.update(this.user_id, user)
          .then((response: any) => {
            this.message = "成功更新使用者資訊 !";
            this.dialog = true;
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },

    close() {
      this.message = "";
      this.dialog = false;
      this.alertDialog = false;
    },

    openAlert() {
      this.message = "確定要註銷帳號嗎?";
      this.alertDialog = true;
    },

    deleteAccount() {
      const user_id = Number(sessionStorage.getItem("user"));
      if (user_id) {
        UserDataService.delete(user_id)
          .then((response: any) => {
            this.authStore.commit("logout");
            this.router.push("/sign-up");
          })
          .catch((e: Error) => {
            console.log(e);
          });
      }
    },
  },
});
</script>
