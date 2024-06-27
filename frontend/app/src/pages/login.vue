<template>
  <v-container class="fill-height d-flex flex-column justify-space-between" fluid>
    <v-row align="center" justify="center" class="flex-grow-1">
      <v-col cols="12" sm="8" md="4">
        <v-card outlined>
          <v-card-title class="text-center">Воход</v-card-title>
          <v-card-text>
            <v-form>
              <v-text-field
                label="Логин"
                outlined
                required
              ></v-text-field>
              <v-text-field
                label="Пароль"
                type="password"
                outlined
                required
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" block>Войти</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-btn text color="secondary" block>Зарегистрироваться</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Login'
}
</script>

<style scoped>

.v-row {
  width: 100%;
}
</style>
