<template>
  <div id="response-container" v-if="hasTravels">
    <span>Estas são as melhores alternativas de viagem para a data selecionada</span>
    <div class="list">
      <div class="company-options">
        <div class="svg-container">
          <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
            id="mdi-clock-check-outline" width="24" height="24" viewBox="0 0 24 24">
            <path
              d="M23.5 17L18.5 22L15 18.5L16.5 17L18.5 19L22 15.5L23.5 17M13.1 19.9C12.7 20 12.4 20 12 20C7.6 20 4 16.4 4 12S7.6 4 12 4 20 7.6 20 12C20 12.4 20 12.7 19.9 13.1C20.6 13.2 21.2 13.4 21.8 13.7C21.9 13.1 22 12.6 22 12C22 6.5 17.5 2 12 2S2 6.5 2 12C2 17.5 6.5 22 12 22C12.6 22 13.2 21.9 13.7 21.8C13.4 21.3 13.2 20.6 13.1 19.9M15.6 14.1L12.5 12.3V7H11V13L14.5 15.1C14.8 14.7 15.2 14.4 15.6 14.1Z" />
          </svg>
        </div>
        <div class="company-name">
          <span class="bold-text">{{ this.travels[0].name }}</span>
          <span class="default-text">Leito: {{ this.travels[0].bed }}</span>
          <span class="default-text">Tempo estimado: {{ this.travels[0].duration }} </span>
        </div>
        <div class="company-price">
          <span class="bold-text">Preço</span>
          <span class="default-text">{{ this.travels[0].price_confort }}</span>
        </div>
      </div>

      <div class="company-options">
        <div class="svg-container">
          <svg xmlns="http://www.w3.org/2000/svg">
            <g data-name="28. Saving" id="_28._Saving">
              <path
                d="M31.47,17.11a5,5,0,0,0-6.53.87l-3.2,3.65A4,4,0,0,0,18,19h-.93a2.54,2.54,0,0,1-1.41-.43A9.38,9.38,0,0,0,3.84,19.74L.29,23.29a1,1,0,0,0,1.42,1.42l3.55-3.55a7.35,7.35,0,0,1,9.29-.92,4.52,4.52,0,0,0,2.52.76H18a2,2,0,0,1,2,2H13a1,1,0,0,0,0,2h8a1,1,0,0,0,.74-.35h0l4.69-5.36a3,3,0,0,1,3-.92L22.4,27.8A3,3,0,0,1,20,29H11.41a4.4,4.4,0,0,0-3.12,1.29,1,1,0,0,0,0,1.42,1,1,0,0,0,1.42,0,2.37,2.37,0,0,1,1.7-.71H20a5,5,0,0,0,4-2l7.8-10.4a1.1,1.1,0,0,0,.15-.8A1.16,1.16,0,0,0,31.47,17.11Z" />
              <path d="M20,16a8,8,0,1,0-8-8A8,8,0,0,0,20,16ZM20,2a6,6,0,1,1-6,6A6,6,0,0,1,20,2Z" />
              <path
                d="M19.29,11.54a1,1,0,0,0,1.42,0l2.83-2.83a1,1,0,0,0,0-1.42L20.71,4.46a1,1,0,0,0-1.42,0L16.46,7.29a1,1,0,0,0,0,1.42ZM20,6.59,21.41,8,20,9.41,18.59,8Z" />
              <path d="M5,5H6V6A1,1,0,0,0,8,6V5H9A1,1,0,0,0,9,3H8V2A1,1,0,0,0,6,2V3H5A1,1,0,0,0,5,5Z" />
            </g>
          </svg>
        </div>
        <div class="company-name">
          <span class="bold-text">{{ this.travels[1].name }}</span>
          <span class="default-text">Leito: {{ this.travels[1].seat }}</span>
          <span class="default-text">Tempo estimado: {{ this.travels[1].duration }} </span>
        </div>
        <div class="company-price">
          <span class="bold-text">Preço</span>
          <span class="default-text">{{ this.travels[1].price_econ }}</span>
        </div>
      </div>
    </div>
  </div>

  <div id="response-container" class="wide" v-else>
    <span>Nenhum dado selecionado</span>
  </div>
</template>

<script>
export default {
  name: "TravelsTo",
  props: ["travels"],
  data() {
    return {
      hasTravels: false
    }
  },
  created() {
    console.log(this.hasTravels);
  },
  watch: {
    travels: function watchTravels() {
      this.hasTravels = this.travels.length > 0 ? true : false
    }
  }
}
</script>

<style>
#response-container {
  display: flex;
  flex-direction: column;
  justify-content: center;

  padding-left: 15px;

  text-align: start;
}


#response-container>span {
  font-weight: 600;
}

.wide {
  align-items: center;
  width: 400px;
}

.svg-container {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 80px;
  height: 90px;

  margin: 10px 0;

  border-bottom-left-radius: 10px;
  border-top-left-radius: 10px;

  background: rgb(84, 164, 230);
}

.svg-container>svg {
  width: 30px;
  height: 30px;

  stroke: white;
  fill: white;
}

.company-options {
  display: flex;
  align-items: center;
}

.company-name {
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;

  padding: 10px 30px;
  height: 70px;
  min-width: 200px;

  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;

  background: #ededed;
}

/* cannot hover all "line" */

/* .company-name:hover {
  background: rgba(128, 128, 128, 0.432);
  transition: 0.3s;
} */

.company-price {
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;

  padding: 10px 30px;
  margin-left: 10px;
  height: 70px;
  width: 20%;
  border-radius: 10px;

  background: #ededed;
}


.bold-text {
  font-weight: 600;
}
</style>