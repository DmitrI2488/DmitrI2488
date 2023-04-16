<template>
    <div>
      <h1>Список мероприятий</h1>
      <ul>
        <li v-for="event in events" :key="event.id">
          <h2>{{ event.name }}</h2>
          <p>{{ event.description_short }}</p>
          <p>Дата: {{ event.starts_at }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
    import axios from 'axios';
    
    export default {
        data() {
        return {
            events: [],
        };
        },
        async mounted() {
          const url = 'http://127.0.0.1:8000/api/events/';

          try {
            const response = await axios.get(url);
            this.events = response.data.values;
          } catch (error) {
            console.error("Error fetching events:", error);
          }
        },

    };
  </script>
  