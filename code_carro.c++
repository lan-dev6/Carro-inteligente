#define IN1 5
#define IN2 4
#define IN3 2
#define IN4 3
#define ENA 10  // PWM - Motor A
#define ENB 9   // PWM - Motor B

int farol = 6;

int motorSpeed = 255; // 0..255




void setup() {
  pinMode(farol, OUTPUT);

  Serial.begin(9600);  // <-- comunicação serial iniciada

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  analogWrite(ENA, motorSpeed);
  analogWrite(ENB, motorSpeed);

  Serial.println("Digite um comando:");
  Serial.println("f = frente | r = re | d = direita | e = esquerda");
}

void Frente() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void Re() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void Esquerda() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void Direita() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void Parar() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

void loop() {

    if(Serial.available()){
        String msg = Serial.readStringUntil('\n');
        Serial.print("Mensagem recebida: ");
        Serial.println(msg);
    

    


    if (msg == "f") {
      Frente();
      Serial.println("Frente");
      delay(2500);
    } else if (msg == "r") {
      Re();
      Serial.println("Ré");
      delay(2500);
    } else if (msg == "d") {
      Direita();
      Serial.println("Direita");
      delay(2500);
    } else if (msg == "e") {
      Esquerda();
      Serial.println("Esquerda");
      delay(2500);
    } 
      else if (msg == "l") {
      digitalWrite(farol, HIGH);
      Serial.println("farol ligado");
      delay(2500);
    }
      else if (msg == "a") {
      digitalWrite(farol, LOW);
      Serial.println("farol desligado");
      delay(2500);
    }    
      else {
      Serial.println("Comando inválido");
    }

    Parar(); // para após o movimento
  }
}
