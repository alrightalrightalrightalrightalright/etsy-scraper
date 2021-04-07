
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>

    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


A scraper app with web interface and a database. The app scrapes an Etsy product data and saves its data in database. Even there is a lot to fix and more features to add this is what I could do with my remianing time after my classes. The datas being scraped are:

* Name - The title of the product
* Price - Price of the product
* Image - The first image shown of the product


### Built With

* Python for data scraping
* Flask for backend
* Postgresql for database
* HTML/CSS/JS for frontend



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

**Running in local**
* Python 3.x.x
* Postgresql 

**Running with Docker**
* Docker Engine

### Installation

**For local:**
1. Clone the repo
   ```
   git clone https://github.com/alrightalrightalrightalrightalright/etsy-scraper.git
   ```
2. Install 
   ```
   pip install -r requirements.txt
   ```
3. Run
   ```
   python main.py
   ```

**For Docker:**

1. Clone the repo
   ```
   git clone https://github.com/alrightalrightalrightalrightalright/etsy-scraper.git
   ```
2. Create Docker Image 
   ```
   docker build -t <tag_of_choice> .
   ```
3. Create and run container
   ```
   docker run -dp <port_of_choice>:3333 <tag_of_choice>
   ```

After installation visit  ```localhost:3333```(or port of choice if you use docker) in your browser to use. 
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

via [email](mailto:k.muratakyildiz@hotmail.com) 

Project Link: [https://github.com/alrightalrightalrightalrightalright/etsy-scraper](https://github.com/alrightalrightalrightalrightalright/etsy-scraper)





