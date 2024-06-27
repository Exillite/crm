<template>
  <v-app>
    <v-app-bar app variant="outlined">
      <v-app-bar-title>CRM</v-app-bar-title>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import { useLocale } from "vuetify";
import control from "@/control";

export default {
  
};
</script>
