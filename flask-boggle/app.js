const form = document.querySelector('#form')
// const input = $("#guess").val();
const word = document.querySelector('#guess')

form.addEventListener('submit', async (e) => {
    e.preventDefault()
    const res = await axios.get('/check-answer')
    
   
})

// const data = async (e) => {
  
// }

