<template>
    <v-container class="text-center">
      <h1>Items</h1>
      <v-row>
        <v-col cols="12" sm="6" md="4" v-for="item in items" :key="item.id">
          <v-card>
            <v-card-title>{{ item.name }}</v-card-title>
            <v-card-subtitle>{{ item.description }}</v-card-subtitle>
            <v-card-actions>
              <v-btn>Action 1</v-btn>
              <v-btn>Action 2</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
</template>
  
<script>
  export default {
    data() {
      return {
        items: [
          {
            id: 1,
            name: "Item 1",
            description: "This is item 1",
          },
          {
            id: 2,
            name: "Item 2",
            description: "This is item 2",
          },
          {
            id: 3,
            name: "Item 3",
            description: "This is item 3",
          },
          {
            id: 4,
            name: "Item 4",
            description: "This is item 4",
          },
          {
            id: 5,
            name: "Item 5",
            description: "This is item 5",
          },
        ],
        //axios = new Axios();
      };
    },
  };
  </script>
  
