<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
    name: "TheDefaultLayout",
});
</script>

<template>
    <v-layout>
        <v-main>
            <slot></slot>
        </v-main>
    </v-layout>
</template>



