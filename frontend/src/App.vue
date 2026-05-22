<script setup>
import { computed, onMounted, onUnmounted, ref } from 'vue'

const answers = ref(null)
const currentQuestionIndex = ref(0)
const selectedOption = ref('')
const answered = ref(false)
const score = ref(0)

const questions = computed(() => {
  if (!answers.value) return []

  return [
    {
      text: 'Which company spent the most on Education in Karnataka ?',
      correctAnswer: answers.value.answer1,
      options: [answers.value.answer1, 'Tech Mahindra Limited', 'Samsung India Electronics Private Limited', 'Larsen And Toubro Limited'],
    },
    {
      text: 'Which company has the spent the highest amount ?',
      correctAnswer: answers.value.answer2,
      options: ['Tech Mahindra Limited', 'Samsung India Electronics Private Limited', 'Larsen And Toubro Limited', answers.value.answer2],
    },
    {
      text: 'Which sector received the most CSR spend in Maharashtra?',
      correctAnswer: answers.value.answer3,
      options: ['Sustainability', answers.value.answer3, 'Livelihood', 'Healthcare'],
    },
    {
      text: 'Which company had the highest CSR spend utilisation rate?',
      correctAnswer: answers.value.answer4,
      options: ['Bharat Petroleum Corporation Limited', answers.value.answer4, 'Jsw Steel Limited', 'Asian Paints Limited'],
    },
    {
      text: 'Which state has most projects in sanitation sector?',
      correctAnswer: answers.value.answer5,
      options: ['Maharashtra', 'Karnataka', 'Tamil Nadu', answers.value.answer5],
    },
    {
      text: 'How many projects are in the education sector ?',
      correctAnswer: answers.value.answer6,
      options: ['12310', '5362', answers.value.answer6, '9882'],
    },
    {
      text: 'What is the total of amount spent by Infosys Limited ?',
      correctAnswer: answers.value.answer7,
      options: ['390400000', answers.value.answer7, '1410300000', '24370000'],
    },
    {
      text: 'Which company spent the highest for Kerala?',
      correctAnswer: answers.value.answer8,
      options: ['Tech Mahindra Limited', 'Samsung India Electronics Private Limited', 'Larsen And Toubro Limited', answers.value.answer8],
    },
    {
      text: 'Which state spent the least ?',
      correctAnswer: answers.value.answer9,
      options: ['Nagaland', 'Manipur', 'Arunachal Pradesh', answers.value.answer9],
    },
    {
      text: 'Which company has spent the highest in Odisha?',
      correctAnswer: answers.value.answer10,
      options: ['Bharat Petroleum Corporation Limited', answers.value.answer10, 'Jsw Steel Limited', 'Asian Paints Limited'],
    },
  ]
})

const currentQuestion = computed(() => questions.value[currentQuestionIndex.value])
const isFinished = computed(() => questions.value.length > 0 && currentQuestionIndex.value >= questions.value.length)
const isCorrect = computed(() => selectedOption.value === currentQuestion.value?.correctAnswer)



function selectOption(option) {
  if (answered.value) return

  selectedOption.value = option
  answered.value = true

  if (option === currentQuestion.value.correctAnswer) {
    score.value++
  }
}

function nextQuestion() {
  currentQuestionIndex.value++
  selectedOption.value = ''
  answered.value = false
}

function playAgain() {
  currentQuestionIndex.value = 0
  selectedOption.value = ''
  answered.value = false
  score.value = 0
}

function handleKeydown(event) {
  if (!currentQuestion.value || answered.value || isFinished.value) return

  const options = currentQuestion.value.options

  if (event.key >= '1' && event.key <= '4') {
    const index = Number(event.key) - 1
    if (options[index]) {
      selectOption(options[index])
    }
  }

  if (event.key === 'ArrowDown' || event.key === 'ArrowRight') {
    event.preventDefault()

    const currentIndex = options.indexOf(selectedOption.value)
    const nextIndex =
      currentIndex === -1 ? 0 : (currentIndex + 1) % options.length

    selectedOption.value = options[nextIndex]
  }

  if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') {
    event.preventDefault()

    const currentIndex = options.indexOf(selectedOption.value)
    const prevIndex =
      currentIndex === -1
        ? options.length - 1
        : (currentIndex - 1 + options.length) % options.length

    selectedOption.value = options[prevIndex]
  }

  if (event.key === 'Enter' && selectedOption.value) {
    selectOption(selectedOption.value)
  }
}

onMounted(async () => {
  const response = await fetch('/answers.json')
  answers.value = await response.json()

  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
})

</script>

<template>
  <main class="min-h-screen bg-quizBg font-montserrat px-5 py-8 text-slate-900">
    <div class="mx-auto flex max-w-3xl flex-col gap-8">
      <header class="flex items-center justify-between gap-4">
        <div>
          <p class="text-sm font-semibold uppercase tracking-[0.25em] text-quizOption">CSR Quiz</p>
          <h1 class="mt-2 text-3xl font-extrabold text-quizQuestion text-[#D9594C] md:text-5xl">Funding Project Quiz</h1>
        </div>

        <div class="rounded-2xl bg-quizScore px-5 py-3 text-center font-extrabold text-[#F8C60F] shadow-md">
          <p class="text-xs uppercase tracking-wider">Score</p>
          <p class="text-2xl">{{ score }}/10</p>
        </div>
      </header>

      <section v-if="!answers" class="rounded-3xl bg-white/70 p-8 text-center shadow-lg">
        Loading quiz...
      </section>

      <section v-else-if="!isFinished" class="rounded-3xl bg-white/80 p-6 shadow-xl md:p-10">
        <p class="mb-4 text-sm font-bold text-quizOption">
          Question {{ currentQuestionIndex + 1 }} of 10
        </p>

        <h2 class="mb-8 text-2xl font-extrabold leading-snug text-quizQuestion md:text-3xl">
          {{ currentQuestion.text }}
        </h2>

        <div class="grid gap-4">
          <label
            v-for="option in currentQuestion.options"
            :key="option"
            class="flex cursor-pointer items-center gap-4 rounded-2xl border-2 border-transparent bg-quizOption px-5 py-4 font-semibold text-[#191919] shadow-sm transition hover:scale-[1.01]"
            :class="{
              'border-green-600 bg-green-600': answered && option === currentQuestion.correctAnswer,
              'border-red-600 bg-red-600': answered && option === selectedOption && option !== currentQuestion.correctAnswer,
              'cursor-not-allowed opacity-80': answered,
            }"
          >
            <input
              type="radio"
              name="answer"
              class="h-5 w-5 accent-quizScore"
              :value="option"
              :checked="selectedOption === option"
              :disabled="answered"
              @change="selectOption(option)"
            />
            <span>{{ option }}</span>
          </label>
        </div>

        <div v-if="answered" class="mt-8 rounded-2xl bg-quizBg p-5 font-bold">
          <p :class="isCorrect ? 'text-green-700' : 'text-red-700'">
            {{ isCorrect ? 'Correct answer!' : 'Incorrect answer.' }}
          </p>
          <p class="mt-2 text-slate-800">
            Correct answer: {{ currentQuestion.correctAnswer }}
          </p>

          <button
            class="mt-5 rounded-full bg-quizScore px-6 py-3 font-extrabold text-slate-900 shadow-md transition hover:scale-105"
            @click="nextQuestion"
          >
            {{ currentQuestionIndex === 9 ? 'See final score' : 'Next question' }}
          </button>
        </div>
      </section>

      <section v-else class="rounded-3xl bg-white/80 p-8 text-center shadow-xl md:p-12">
        <p class="text-sm font-bold uppercase tracking-[0.25em] text-quizOption">Quiz complete</p>
        <h2 class="mt-4 text-4xl font-extrabold text-quizQuestion md:text-6xl">
          Final Score: {{ score }}/10
        </h2>

        <button
          class="mt-8 rounded-full bg-quizScore px-8 py-4 text-lg font-extrabold text-slate-900 shadow-md transition hover:scale-105"
          @click="playAgain"
        >
          Play again
        </button>
      </section>
    </div>
  </main>
</template>
