<template>
  <div>
    <h1>Список мероприятий</h1>
    <label for="category">Выберите категорию:</label>
    <select id="category" v-model="selectedCategory" @change="fetchEvents">
      <option v-for="category in categories" :key="category.id" :value="category.id">
        {{ category.name }}
      </option>
    </select>
    <div v-if="loading" class="loader">Загрузка...</div>
    <div v-else>
      <ul>
        <li v-for="event in events" :key="event.id">
          <h2>{{ event.name }}</h2>
          <p>{{ event.description_short }}</p>
          <p>Дата: {{ event.starts_at }}</p>
        </li>
      </ul>
  </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      categories: [],
      selectedCategory: "525",
      events: [],
      loading: false,
    };
  },
  async mounted() {
    await this.fetchCategories();
    this.fetchEvents();
  },
  methods: {
    async fetchCategories() {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/categories/"
        );
        this.categories = response.data.values;
      } catch (error) {
        console.error("Error fetching categories:", error);
      }
    },
    async fetchEvents() {
      this.loading = true;
      const url = 'http://127.0.0.1:8000/api/events/';
      try {
        const response = await axios.get(url, { params: { category_id: this.selectedCategory } });
        console.log(response.data )
        this.events = response.data.values;
      } catch (error) {
        console.error("Error fetching events:", error);
      } finally {
        this.loading = false; // заканчиваем загрузку
      }
    },
  },
};
</script>


  
  