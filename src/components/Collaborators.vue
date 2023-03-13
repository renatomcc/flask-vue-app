<template>
  <div class="container">
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/journal/bootstrap.min.css"
      integrity="sha384-QDSPDoVOoSWz2ypaRUidLmLYl4RyoBWI44iA5agn6jHegBxZkNqgm2eHb6yZ5bYs"
      crossorigin="anonymous"
    />
    <h1>Lista de Colaboradores</h1>
    <div class="d-flex flex-wrap justify-content-center">
      <div
        v-for="(collaborator, index) in collaborators"
        :key="index"
        class="card m-3"
        style="width: 12rem"
      >
        <img
          :src="collaborator.image"
          :alt="collaborator.name"
          class="card-img-top"
        />
        <div class="card-body d-flex flex-column">
          <h5 class="card-title">{{ collaborator.name }}</h5>
          <p class="card-text">{{ collaborator.occupation }}</p>

          <div class="rates">
            <ul class="unstyled list-unstyled">
              <li>
                <div class="rate flex-grow-1 d-flex justify-content-between">
                  <span>Qualidade: </span>
                  {{ collaborator.work_quality }}
                </div>
              </li>
              <li>
                <div class="rate flex-grow-1 d-flex justify-content-between">
                  <span>Empenho: </span>
                  {{ collaborator.effort }}
                </div>
              </li>
              <li>
                <div class="rate flex-grow-1 d-flex justify-content-between">
                  <span>Pontualidade: </span>
                  {{ collaborator.ponctuality }}
                </div>
              </li>
              <li>
                <div class="rate flex-grow-1 d-flex justify-content-between">
                  <span>Criatividade: </span>
                  {{ collaborator.creativity }}
                </div>
              </li>
              <li>
                <div class="rate flex-grow-1 d-flex justify-content-between">
                  <span>Metas: </span>
                  {{ collaborator.goals_delivery }}
                </div>
              </li>
            </ul>
          </div>

          <div class="mt-auto d-flex justify-content-between">
            <button
              type="button"
              class="btn btn-primary"
              data-toggle="modal"
              data-target="#collaboratorModal"
              @click="handleModal(collaborator)"
            >
              Update
            </button>

            <button
              class="btn btn-danger btn-sm ml-2"
              @click="deleteCollaborator(collaborator)"
            >
              Delete
            </button>
          </div>
        </div>
        <div
          id="collaboratorModal"
          tabindex="-1"
          role="dialog"
          aria-labelledby="collaboratorModalLabel"
          aria-hidden="true"
          v-if="showModal"
          class="modal fixed-top d-flex align-items-center justify-content-center overflow-hidden"
        >
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="collaboratorModalLabel">
                  Atualizar {{ collaborator.name }}
                </h5>
                <button
                  type="button"
                  class="close"
                  data-dismiss="modal"
                  aria-label="Close"
                  @click="closeModal"
                >
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <div class="form-group">
                  <label for="occupation-select">Occupation:</label>
                  <select
                    class="form-control"
                    id="occupation-select"
                    v-model="selectedCollaborator.occupation"
                    v-if="selectedCollaborator"
                  >
                    <option value="Desenvolvedor">Desenvolvedor</option>
                    <option value="Designer">Designer</option>
                    <option value="Marketing">Marketing</option>
                    <option value="Gestão">Gestão</option>
                  </select>
                </div>

                <div class="form-group">
                  <label for="qualidade-input">Qualidade do trabalho:</label>
                  <input
                    type="number"
                    class="form-control"
                    id="qualidade-input"
                    v-model="selectedCollaborator.work_quality"
                    v-if="selectedCollaborator"
                    :max="5"
                    :min="0"
                    @input="validateInput(selectedCollaborator.name)"
                  />
                  <div v-if="!selectedCollaborator.validInput">
                    Apena valores de 0 - 5
                  </div>
                </div>

                <div class="form-group">
                  <label for="empenho-input">Empenho:</label>
                  <input
                    type="number"
                    class="form-control"
                    id="empenho-input"
                    v-model="selectedCollaborator.effort"
                    v-if="selectedCollaborator"
                    :max="5"
                    :min="0"
                  />
                </div>

                <div class="form-group">
                  <label for="pontualidade-input">Pontualidade:</label>
                  <input
                    type="number"
                    class="form-control"
                    id="pontualidade-input"
                    v-model="selectedCollaborator.ponctuality"
                    v-if="selectedCollaborator"
                    :max="5"
                    :min="0"
                  />
                </div>

                <div class="form-group">
                  <label for="criatividade-input">Criatividade:</label>
                  <input
                    type="number"
                    class="form-control"
                    id="criatividade-input"
                    v-model="selectedCollaborator.creativity"
                    v-if="selectedCollaborator"
                    :max="5"
                    :min="0"
                  />
                </div>

                <div class="form-group">
                  <label for="metas-input">Metas:</label>
                  <input
                    type="number"
                    class="form-control"
                    id="metas-input"
                    v-model="selectedCollaborator.goals_delivery"
                    v-if="selectedCollaborator"
                    :max="5"
                    :min="0"
                  />
                </div>
              </div>
              <div class="modal-footer">
                <button
                  type="button"
                  class="btn btn-secondary"
                  data-dismiss="modal"
                  @click="handleModal"
                >
                  Close
                </button>
                <button
                  type="button"
                  class="btn btn-primary"
                  @click="updateCollaborator(collaborator.name)"
                >
                  Confirmar
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CollaboratorList",
  data() {
    return {
      collaborators: [
        {
          name: "Renato",
          image: "example.org",
          occupation: "Dev",
          work_quality: 5,
          effort: 5,
          ponctuality: 5,
          creativity: 5,
          goals_delivery: 5,
          validInput: true,
        },
      ],
      selectedOccupation: "Dev",
      updatedQualidade: 5,
      updatedEmpenho: 5,
      updatedPontualidade: 5,
      updatedCriatividade: 5,
      updatedMetas: 5,
      showModal: false,
      selectedCollaborator: 5,
    };
  },

  methods: {
    getCollaborators() {
      const path = "http://localhost:5000/collaborators";
      axios.get(path).then((res) => (this.collaborators = res.data));
    },
    handleModal(collaborator: any) {
      this.selectedCollaborator = collaborator;
      this.showModal = !this.showModal;
    },

    closeModal() {
      this.showModal = false;
    },

    validateInput(collaboratorName: string) {
      const collaboratorIndex = this.collaborators.findIndex(
        (c) => c.name === collaboratorName
      );
      if (this.collaborators[collaboratorIndex].work_quality > 5) {
        this.collaborators[collaboratorIndex].work_quality = 5;
      } else if (this.collaborators[collaboratorIndex].work_quality < 0) {
        this.collaborators[collaboratorIndex].work_quality = 0;
      }
    },

    updateCollaborator(collaboratorName: string) {
      this.showModal = false;
      const collaboratorIndex = this.collaborators.findIndex(
        (c) => c.name === collaboratorName
      );
      this.collaborators[collaboratorIndex].occupation =
        this.selectedOccupation;
      this.collaborators[collaboratorIndex].work_quality =
        this.updatedQualidade;
      this.collaborators[collaboratorIndex].effort = this.updatedEmpenho;
      this.collaborators[collaboratorIndex].ponctuality =
        this.updatedPontualidade;
      this.collaborators[collaboratorIndex].creativity =
        this.updatedCriatividade;
      this.collaborators[collaboratorIndex].goals_delivery = this.updatedMetas;
    },

    deleteCollaborator(collaborator: any) {
      const index = this.collaborators.indexOf(collaborator);
      this.collaborators.splice(index, 1);
    },
  },

  components: {},

  created() {
    this.getCollaborators();
  },
});
</script>
