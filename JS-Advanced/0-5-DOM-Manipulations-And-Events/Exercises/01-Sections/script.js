function create(words) {
   for (const word of words) {
      const div = document.createElement('div');
      const p = document.createElement('p');
      p.textContent = word;
      p.style.display = 'none';
      div.appendChild(p);
      div.addEventListener('click', showChildElement);
      document.getElementById('content').appendChild(div);
   }

   function showChildElement(event) {
      event.target.querySelector('p').style.display = 'block';
   }
}
