function confirmPassword() {
    var password = prompt("Entrez votre mot de passe :");
    var confirmPassword = prompt("Confirmez votre mot de passe :");
  
    if (password === confirmPassword) {
      alert("Le mot de passe est correct.");
      window.location.href = "auth";
    } else {
      alert("Les mots de passe ne correspondent pas.");
    }
  }

  function confirmPassword2(pw1,pw2) {
    var password = document.getElementById(pw1).value;
    var confirmPassword = document.getElementById(pw2).value;
  
    if (pw1 === pw2s) {
      alert("Le mot de passe est correct.");
      window.location.href = "auth";
    } else {
      alert("Les mots de passe ne correspondent pas.");
    }
  }