<template>
    <v-container class="text-center">
        <v-card elevation="2" tile max-width="500" class="ma-auto">
            <v-card-title>建立市場</v-card-title>
            <v-form class="ma-3">
                <v-text-field class="ma-3" v-model="state.market_name" label="市場名稱"
                    :error-messages="v$.market_name.$errors.map((e: any) => e.$message)" 
                    @input="v$.market_name.$touch"
                    @blur="v$.market_name.$touch">
                </v-text-field>
            </v-form>
            <v-btn class="ma-3" color="blue-lighten-1" @click="submitForm">建立市場</v-btn>
        </v-card>
    </v-container>
</template>
<script lang="ts">
import useValidate from "@vuelidate/core";
import { required } from '@vuelidate/validators';
import { computed, defineComponent, reactive } from 'vue';
import MarketDataService from "../../../services/MarketDataService";
import { useRouter } from "vue-router";

export default defineComponent({
    name: "CreateMarket",
    setup() {
        const router = useRouter();

        const state = reactive({
            market_name: "",
        });

        const rules = computed(() => {
            return {
                market_name: { required },
            };
        });

        const v$ = useValidate(rules, state);

        return { state, v$, router };
    },
    methods: {
        submitForm() {
            const userId = Number(sessionStorage.getItem("user"));
            if(userId) {
                const market = {
                user_id: userId,
                market_name: this.state.market_name
            }
            MarketDataService.create(market).then((response: any) => {
                console.log(response.data);
                this.router.go(0);
            }).catch((e: Error) => {
                console.log(e);
            })
            }
        }
    }
})
</script>