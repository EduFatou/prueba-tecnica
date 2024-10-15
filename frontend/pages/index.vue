<template>
  <div class="container">
    <h1 class="title">Lista de Productos</h1>
    <table class="product-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Precio</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto in productos" :key="producto.id">
          <td>{{ producto.id }}</td>
          <td>{{ producto.name }}</td>
          <td>{{ producto.price }} €</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const productos = ref([])

onMounted(async () => {
  const response = await fetch('http://localhost:8000/api/products/')
  productos.value = await response.json()
})
</script>

<style src="@/assets/css/products.css"></style>
