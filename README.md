# Embedded Smart Medication Organizer WebApp
<!--
*** Thanks for checking out my groups text lab. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
-->


### Built With

* [Python](https://python.org/)
* [Anvil](https://anvil.works/)


<!-- GETTING STARTED -->
## Topic
The Smart Medication Organizer (SMO) is a wirelessly programmable, internet-of-things device that assists in the consistent self-administration of pharmaceuticals by patients, in order to reduce nonadherence. 

To accomplish this goal, the SMO provides timed auditory and visual indications to signal to the user to take their medications. 

The device encompasses:
* a screen
* a speaker
* a wall outlet power supply
* a microcontroller (TI MSP432)
* six medication compartments, each with an LED. 

The electronics are located inside an aesthetically pleasing wooden box to hide the details from the user. 

The device connects to a user’s wireless local area network, where it can be reached from the user’s personal or mobile device through a web application, which is provided in this repository, 

The web application allows the user to configure when they need to take which medications, which compartment each medication is in, and dosage information. 

This information is encrypted to protect the user’s data privacy and then sent to the device, where events are scheduled based on the information provided. 

When it is time for the user to take their medication, the speaker plays a sound to draw the user’s attention, the LEDs indicate in which compartment the medication to take is located, and the screen displays other necessary dosage information. 

The user can stop the sound and LEDs by pressing an okay button to confirm they have taken their medication, and the next medication event will be scheduled automatically. 

The device is a compact, easy-to-use, and affordable solution to unintentional nonadherence. 


### Go to the User-Interface

http://tiny.cc/6OhmsApartWebApp


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Sai Rajuladevi: https://www.linkedin.com/in/sai-rajuladevi/

Forrest Feaser: https://github.com/fdfea


Project Link: https://github.com/sr9dc/CapstoneWebApp

Embedded Work: https://github.com/fdfea/smart-medication-organizer







