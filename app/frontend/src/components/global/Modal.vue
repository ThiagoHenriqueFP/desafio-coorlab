<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-exclamation-square svg-header"
            viewBox="0 0 16 16">
            <path
              d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z" />
            <path
              d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z" />
          </svg>
        </slot>
      </header>

      <section class="modal-body">
        <slot name="body">
          <span class="bold-text warning-text">Insira os valores para realizar a cotação.</span>
        </slot>
      </section>

      <footer class="modal-footer">
        <button type="button" class="default-btn" @click="close">
          Fechar
        </button>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalError",
  props: {
    show: Boolean
  },
  methods: {
    close() {
      this.$emit('close');
    }
  }
}
</script>

<style>
.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #FFFFFF;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;

  width: 500px;

  border-radius: 10px;
}

.warning-text {
  font-size: 20px;
}

.modal-header,
.modal-footer {
  display: flex;
  margin: 10px;
}

.modal-header {
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.modal-footer>button {
  padding: 10px;
}

.svg-header {
  stroke: var(--background-btn-blue);
  fill: var(--background-btn-blue);
  width: 52px;
  margin: 50px 40px 20px 40px;
}
</style>