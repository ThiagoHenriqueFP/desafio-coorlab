<template>
  <div id="container-travel">
    <header id="travel-calc-header">
      <svg class="smaller" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
        id="mdi-truck-delivery-outline" width="24" height="24" viewBox="0 0 24 24">
        <path
          d="M18 18.5C18.83 18.5 19.5 17.83 19.5 17C19.5 16.17 18.83 15.5 18 15.5C17.17 15.5 16.5 16.17 16.5 17C16.5 17.83 17.17 18.5 18 18.5M19.5 9.5H17V12H21.46L19.5 9.5M6 18.5C6.83 18.5 7.5 17.83 7.5 17C7.5 16.17 6.83 15.5 6 15.5C5.17 15.5 4.5 16.17 4.5 17C4.5 17.83 5.17 18.5 6 18.5M20 8L23 12V17H21C21 18.66 19.66 20 18 20C16.34 20 15 18.66 15 17H9C9 18.66 7.66 20 6 20C4.34 20 3 18.66 3 17H1V6C1 4.89 1.89 4 3 4H17V8H20M3 6V15H3.76C4.31 14.39 5.11 14 6 14C6.89 14 7.69 14.39 8.24 15H15V6H3M10 7L13.5 10.5L10 14V11.5H5V9.5H10V7Z" />
      </svg>
      <span class="default-white">Calculadoda de Viagem</span>
    </header>
    <div id="content-travel">
      <div id="options">
        <div id="options-header">
          <svg class="smaller" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
            <g data-name="28. Saving" id="_28._Saving">
              <path
                d="M31.47,17.11a5,5,0,0,0-6.53.87l-3.2,3.65A4,4,0,0,0,18,19h-.93a2.54,2.54,0,0,1-1.41-.43A9.38,9.38,0,0,0,3.84,19.74L.29,23.29a1,1,0,0,0,1.42,1.42l3.55-3.55a7.35,7.35,0,0,1,9.29-.92,4.52,4.52,0,0,0,2.52.76H18a2,2,0,0,1,2,2H13a1,1,0,0,0,0,2h8a1,1,0,0,0,.74-.35h0l4.69-5.36a3,3,0,0,1,3-.92L22.4,27.8A3,3,0,0,1,20,29H11.41a4.4,4.4,0,0,0-3.12,1.29,1,1,0,0,0,0,1.42,1,1,0,0,0,1.42,0,2.37,2.37,0,0,1,1.7-.71H20a5,5,0,0,0,4-2l7.8-10.4a1.1,1.1,0,0,0,.15-.8A1.16,1.16,0,0,0,31.47,17.11Z" />
              <path d="M20,16a8,8,0,1,0-8-8A8,8,0,0,0,20,16ZM20,2a6,6,0,1,1-6,6A6,6,0,0,1,20,2Z" />
              <path
                d="M19.29,11.54a1,1,0,0,0,1.42,0l2.83-2.83a1,1,0,0,0,0-1.42L20.71,4.46a1,1,0,0,0-1.42,0L16.46,7.29a1,1,0,0,0,0,1.42ZM20,6.59,21.41,8,20,9.41,18.59,8Z" />
              <path d="M5,5H6V6A1,1,0,0,0,8,6V5H9A1,1,0,0,0,9,3H8V2A1,1,0,0,0,6,2V3H5A1,1,0,0,0,5,5Z" />
            </g>
          </svg>
          <span>Calcule o Valor da Viagem</span>
        </div>
        <label for="cities">Destino</label>
        <select name="cities" class="input-field" id="cities-list" placeholder="cidades" v-model="city">
          <option v-for="city in cities" v-bind:key="city">{{ city }}</option>
        </select>

        <label for="date">Data</label>
        <input type="date" v-model="dateField" class="input-field" name="date" id="date-field">
        <button class="default-btn" @click="selectCity(this.city)">Buscar</button>
        <Modal v-if="show" @close="closeModal" />
      </div>
      <TravelsTo :travels="this.travels" />
    </div>
    <button class="clear-btn" @click="unselect">Limpar</button>

  </div>
</template>

<script>
import TravelsTo from "./TravelsTo.vue"
import Modal from "../global/Modal.vue";

import axios from "../../services/axios";


export default {
  name: "TravelCalc",
  components: {
    TravelsTo,
    Modal
  },
  data() {
    return {
      cities: {},
      travels: [],
      selected: false,
      dateField: null,
      show: false,
      city: null
    }
  },
  created() {
    this.getCities();
  },
  methods: {
    getCities() {
      axios.get("/api/travels/cities")
        .then((result) => this.cities = result.data)
        .catch(error => console.log(error));
    },
    selectCity(city) {
      if (this.dateField == null || this.city == null) {
        console.log("hello")
        this.showModal()
      } else {
        axios.get(`/api/travels/to/${city}`)
          .then(result => {
            this.travels = result.data
            console.log(this.travels)
            this.selected = true;
          })
          .catch(error => console.log(error));
      }
    },
    unselect() {
      this.selected = false;
      this.travels = [];
      this.city = null;
      this.dateField = null;
    },
    showModal() {
      this.show = true;
      console.log(this.show)
    },
    closeModal() {
      this.show = false;
    }
  }
}

</script>

<style>
#container-travel {
  display: flex;
  flex-direction: column;

  height: max-content;
  max-width: max-content;
  margin: auto;

  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;

  -webkit-box-shadow: 0px 0px 39px -7px rgba(0, 0, 0, 0.56);
  -moz-box-shadow: 0px 0px 39px -7px rgba(0, 0, 0, 0.56);
  box-shadow: 0px 0px 39px -7px rgba(0, 0, 0, 0.56);
}

#travel-calc-header {
  display: flex;
  align-items: center;

  padding: 20px;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;

  background: #262a3b;
}

#content-travel {
  display: flex;

  height: 100%;
  padding: 20px;
}

#options {
  background: #ededed;
  padding: 25px;
  min-width: max-content;

  display: flex;
  flex-direction: column;

  width: 300px;
}

#options-header {
  display: flex;
  align-items: center;
  justify-content: center;

  color: #262a3b;
  font-size: 18px;
  font-weight: 600;
  padding: 10px 0;
}

.input-field {
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  border: 1px solid rgba(128, 128, 128, 0.432);
  background-color: white;

  color: grey;
}

.input-field[type="date"] {
  padding: 10px;
  margin-bottom: 30px;
}

label {
  margin: 10px 0;
  margin-right: auto;

  font-size: 14px;
}

.default-btn {
  width: 140px;

  margin: 30px auto;
  padding: 5px;
  border-radius: 5px;
  border: none;

  background: rgb(84, 164, 230);
}

.default-btn:hover {
  cursor: pointer;
}

.clear-btn {
  margin: 0 20px 10px 0;

  margin-left: auto;

  width: 140px;
  height: 25px;
  padding: 5px;

  background: #FFBF00;
  border: none;
  border-radius: 5px;

  cursor: pointer;
}
</style>