# Differential-Privacy
Differential Privacy methods

# What it is

![Image explaining Differential Privay](https://www.accessnow.org/cms/assets/uploads/2017/10/local-vs-global-cropped.png)

Differential privacy is just creating a way for whoever is getting the data to get slightly altered data. For example, if Jeff is creating a data set, and you don't trust Jeff (I mean, who trusts Jeff, right?), you can answer a question and say no to a question like *Do you jump a lot?* (even though you do) and the algorithm _might_ change it to yes. This way you can say, I answered no but it changed to yes through the algorithm. This creates a way for you to not completely mess up a survey but allow your information to stay private.

In this version, the algorithm is basically fliping a coin and if it lands on heads, it will keep that value the same. If it is tails on the other hand, it will flip the coin again, and then if it is heads, it will change the value to yes, if tails, then it changes the value to no.

![Image showing how this version of differential privacy works](https://miro.medium.com/max/1082/1*oOkcVZUn4hrsxompg4Ik_g.png)

**Coding in python? Check out [DiffPriv](https://github.com/Quantalabs/DiffPriv)**
