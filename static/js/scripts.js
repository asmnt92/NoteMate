// ✅ Dashboard
const addNoteBtn = document.getElementById("addNoteBtn");
const closeBtn = document.getElementById("closeBtn");
const noteFormWrapper = document.getElementById("noteFormWrapper");

if (addNoteBtn && closeBtn && noteFormWrapper) {
  addNoteBtn.addEventListener("click", () => {
    noteFormWrapper.classList.remove("hidden");
  });

  closeBtn.addEventListener("click", () => {
    noteFormWrapper.classList.add("hidden");
  });
}


// ✅ Sign-In
const showPassword_signIn = document.getElementById('showPassword-signIn');
const password_signIn = document.getElementById('password-signIn');

if (showPassword_signIn && password_signIn) {
  showPassword_signIn.addEventListener('change', function() {
    const type = this.checked ? 'text' : 'password';
    password_signIn.type = type;
  });
}


// ✅ Sign-Up
const showPassword = document.getElementById('showPassword');
const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirm_password');

if (showPassword && password && confirmPassword) {
  showPassword.addEventListener('change', function() {
    const type = this.checked ? 'text' : 'password';
    password.type = type;
    confirmPassword.type = type;
  });
}


// Modal for sign-up
const openModalBtnsSignUp = document.querySelectorAll('.openModalBtn-signUp'); 
const signupModal1 = document.getElementById('signupModal-signUp');
const closeModalBtn1 = document.getElementById('closeModalBtn-signUp');

// Modal for sign-in
const openModalBtnsSignIn = document.querySelectorAll('.openModalBtn-signIn'); 
const signupModal2 = document.getElementById('signupModal-signIn');
const closeModalBtn2 = document.getElementById('closeModalBtn-signIn');

// ----- Sign-Up Modal Logic -----
if (signupModal1 && closeModalBtn1) {
  openModalBtnsSignUp.forEach(btn => {
    btn.addEventListener('click', () => {
      // Close Sign-In modal if open
      signupModal2.classList.add('hidden');
      // Open Sign-Up modal
      signupModal1.classList.remove('hidden');
    });
  });

  closeModalBtn1.addEventListener('click', () => {
    signupModal1.classList.add('hidden');
  });

  signupModal1.addEventListener('click', (e) => {
    if (e.target === signupModal1) signupModal1.classList.add('hidden');
  });
}

// ----- Sign-In Modal Logic -----
if (signupModal2 && closeModalBtn2) {
  openModalBtnsSignIn.forEach(btn => {
    btn.addEventListener('click', () => {
      // Close Sign-Up modal if open
      signupModal1.classList.add('hidden');
      // Open Sign-In modal
      signupModal2.classList.remove('hidden');
    });
  });

  closeModalBtn2.addEventListener('click', () => {
    signupModal2.classList.add('hidden');
  });

  signupModal2.addEventListener('click', (e) => {
    if (e.target === signupModal2) signupModal2.classList.add('hidden');
  });
}

