# DaiSLab Image Annotator Web Application

## 프로젝트 목적 및 용도
vgg 연구팀에서 개발한 Vgg Image Annotator(VIA)를 활용하여 메타데이터를 생성한다.<br>
이렇게 생성된 메타데이터들과 원본이미지들을 로컬환경에서 따로 관리할 경우 분실과 회손의 위험이 존재한다.<br>
따라서 각 기업별로 ID를 할당하여 메타데이터와 이미지들을 파일 업로드 및 유용한 관리를 할 수 있는 웹사이트가 필요하였다.<br>
상기 프로젝트는 VIA를 프로젝트에 이식하여 해당 웹사이트상에서도 어노테이션을 진행할 수 있게 하였으며 본인 계정을 통해 파일들을 업로드 및 관리할 수 있다.
최근 제조기업들의 스마트팩토리화가 가속화되고 있는 상황에서 Digital Transformation(DT)는 필수적인 요소가 되었다. 해당 웹은 전통적인 제조 기업과 제조AI기업간의 원활한 DB관리체계를 지원할 것으로 기대된다.

## 요구사항 기술

### 1. 기능적 요구사항

via페이지에서 VGG Image Annotator(VIA)를 통해 이미지의 메타데이터를 생성한다.

로그인을 통해 사용자 인증을 한다.

생성한 메타데이터와 원본이미지를 DB에 업로드한다.

업로드한 데이터들은 index페이지에 보여진다. 

사용자가 업로드된 정보의 상세 정보를 볼 수 있도록 한다.

상세정보를 편집 및 삭제 할 수 있도록한다.

사용자가 원하는 데이터를 찾을 수 있도록 검색하도록 한다.

### 2. 비기능적 요구사항

사용자가 업로드한 DB가 안전하게 업로드 및 보관되어야한다.

사용자의 정보 보안유지가 잘 되어야한다.

host의 요청 지연이 불만을 느낄 정도로 생겨서는 안된다.

## 구현 기능

- Annotator
- 로그인 기능 (회원가입 기능은 제외함 admin에서 ID를 생성하여 할당하는 방식)
- CRUD 구현
- 업로드 파일 검색 기능 구현
- 파일 다운로드 기능 구현
- 
### 1. VGG Image Annotator
![image](https://github.com/ChangZero/DaisLab_VIA/assets/97018869/72ad5405-7ad6-4875-a41a-19908aef760b)

VGG연구팀에서 만든 VIA를 django 프로젝트에 이식하였다. 

### 2. 로그인 기능 구현

![image](https://github.com/ChangZero/DaisLab_VIA/assets/97018869/b875dc20-e35c-491f-b5fd-db5da15920c6)

로그인기능을 구현하여 각 기업별로 파일을 업로드 할 수 있도록 하였다. 

로그인을 하면 유저가 업로드한 파일들이 업로드 날짜 기준으로 정렬되어 나타난다.

![image](https://github.com/ChangZero/DaisLab_VIA/assets/97018869/30327e97-4fa5-4a2f-a551-967f58915f7f)



### 3. CRUD 구현(Create, Read, Update, Delete)

- Create 기능
    ![image](https://github.com/ChangZero/DaisLab_VIA/assets/97018869/810658a5-8b62-49cb-96f9-ebe0cd2383ca)
   
    Title, Image, Metadata 필드는 반드시 입력(선택)되어야 업로드가 된다. 
    
    또한 Image는 jpg, png형식으로 받도록 , Metadata는 csv, json형식으로만 받도록 설정하였다.
    
- Read 기능
    
    ![image](https://github.com/ChangZero/DaisLab_VIA/assets/97018869/7acba94f-d028-4321-9e3f-2fb33fde999e)
    
    index페이지에서 title(제목)을 선택하면 상세한 정보를 확인 할 수 있다. 
    
    index페이지에서는 편집(edit)과 삭제(delete)가 지원된다.
    
- Update 기능(편집)
    
    ![image](https://github.com/ChangZero/DaisLab_VIA/assets/97018869/c2a2fb8b-276c-4918-a9ae-54454a8eb570)

    ![image](https://github.com/ChangZero/DaisLab_VIA/assets/97018869/4fca28a2-1d79-471a-b82c-e53e0941f5d1)

    
- Delete 기능
    
    ![image](https://github.com/ChangZero/DaisLab_VIA/assets/97018869/075f6bc8-fa75-47cd-a1b7-1978b3ca23ea)

    

### 3. 업로드된 파일 검색기능

![image](https://github.com/ChangZero/DaisLab_VIA/assets/97018869/eb4cd27b-588f-4e66-9ea7-91cb12e79c9f)


### 4. 파일 다운로드 기능 구현

![image](https://github.com/ChangZero/DaisLab_VIA/assets/97018869/3614a4fe-5b99-4335-b473-4185ee5e9d2c)

## License
BSD-2-Clause

<hr>

# VGG Image Annotator (외부 리소스)

VGG Image Annotator (VIA) is a simple and standalone manual image annotation 
software. VIA runs in a web browser and does not require any installation or setup. 
The complete VIA software fits in a single self-contained HTML page of size 
less than 400 Kilobyte that runs as an offline application in most modern web browsers.

VIA is an [open source](https://gitlab.com/vgg/via) project based solely on 
HTML, Javascript and CSS (no dependency on external libraries). VIA is 
developed at the [Visual Geometry Group](http://www.robots.ox.ac.uk/~vgg/) (VGG) 
and released under the BSD-2 clause [license](https://gitlab.com/vgg/via/blob/master/LICENSE)
which allows it to be useful for both academic projects and commercial applications.

## Screenshots
<img src="via-2.x.y/doc/screenshots/via_demo_screenshot2_via-2.0.2.jpg" alt="Screenshot showing basic image annotation" title="Screenshot showing basic image annotation" height="370">
<img src="via-2.x.y/doc/screenshots/via_face_demo_screenshot4.jpg" alt="Screenshot of VIA being used for face annotation" title="Screenshot of VIA being used for face annotation" height="370">
<img src="via-2.x.y/doc/screenshots/via_face_track_demo_screenshot1.jpg" alt="Screenshot of VIA being used for face track annotation" title="Screenshot of VIA being used for face track annotation" height="370">

## Demo
We have created self contained demo to illustrate the usage of VIA. These demo
have been preloaded with some sample images. Furthermore, we have 
also added some sample manual annotations to these demo. These demo applications 
are very useful to get familiar with the commonly used features of VIA.
  * [Basic Image Annotation Demo](http://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html)
  * [Face Annotation Demo](http://www.robots.ox.ac.uk/~vgg/software/via/via_face_demo.html)
  * [Remote Image Annotation Demo](http://www.robots.ox.ac.uk/~vgg/software/via/via_wikimedia_demo.html)
  * [Face Track Annotation Demo](http://www.robots.ox.ac.uk/~vgg/software/via/docs/face_track_annotation.html)

## Download
Detailed instructions for download of VIA3 are available at http://www.robots.ox.ac.uk/~vgg/software/via/

## Docs
 * User Guide : this can be accessed from the menubar "Help -> Getting Started"
 * [Face Track Annotation](http://www.robots.ox.ac.uk/~vgg/software/via/docs/face_track_annotation.html)
 * [Setting up a project containing remotely hosted images](http://www.robots.ox.ac.uk/~vgg/software/via/docs/via_with_remote_images.html)
 * [A blog post describing VIA and its open source ecosystem.](http://www.robots.ox.ac.uk/~vgg/blog/vgg-image-annotator.html)

## Open Source Ecosystem
The development of VIA software began in August 2016 and the first public
release of version 1 was made in April 2017. Many new advanced features
for image annotation were introduced in version 2 which was released in June 2018. 
Recently released version 3 of VIA software supports annotation of audio and video. 
As of May 2019, the VIA software has been used more than 600,000 times (+150,000 unique pageviews).

We have nurtured a large and thriving open source community which not
only provides feedback but also contributes code to add new features
and improve existing features in the VIA software. The open source
ecosystem of VIA thrives around its [source code repository](https://gitlab.com/vgg/via)
hosted by the Gitlab platform. Most of our users report issues and
request new features for future releases using the [issue portal](https://gitlab.com/vgg/via/issues). 
Many of our users not only submit bug reports but also suggest a potential
fix for these software issues. Some of our users also contribute code
to add new features to the VIA software using the [merge request portal](https://gitlab.com/vgg/via/merge_requests). 

We welcome all forms of contributions (code update, documentation, bug reports, etc) from users. 
Such contributions must must adhere to the existing [license](https://gitlab.com/vgg/via/blob/master/LICENSE) of 
the VIA project.

## Citation
If you use this software, please cite it as follows:

<cite>Abhishek Dutta and Andrew Zisserman. 2019. <a href="docs/dutta2019vgg_arxiv.pdf">The VIA Annotation Software for Images, Audio and Video</a>. In Proceedings of the 27th ACM International Conference on Multimedia (MM ’19), October 21–25, 2019, Nice, France. ACM, New York, NY, USA, 4 pages. https://doi.org/10.1145/3343031.3350535</cite>.

```
@inproceedings{dutta2019vgg,
  author = {Dutta, Abhishek and Zisserman, Andrew},
  title = {The {VIA} Annotation Software for Images, Audio and Video},
  booktitle = {Proceedings of the 27th ACM International Conference on Multimedia},
  series = {MM '19},
  year = {2019},
  isbn = {978-1-4503-6889-6/19/10},
  location = {Nice, France},
  numpages = {4},
  url = {https://doi.org/10.1145/3343031.3350535},
  doi = {10.1145/3343031.3350535},
  publisher = {ACM},
  address = {New York, NY, USA},
} 

@misc{dutta2016via,
  author = "Dutta, A. and Gupta, A. and Zissermann, A.",
  title = "{VGG} Image Annotator ({VIA})",
  year = "2016",
  howpublished = "http://www.robots.ox.ac.uk/~vgg/software/via/",
  note = "Version: X.Y.Z, Accessed: INSERT_DATE_HERE" 
}
```

## Developer Resources
**Please send all pull requests for a specific version (e.g. via-2.x.y) to their respective branch (e.g. branch via-2.x.y). All contributions made to VIA code repository will be licensed under the [BSD-2 clause license](https://gitlab.com/vgg/via/blob/master/LICENSE).**

The VIA application is made up of the following three files:
 * [index.html](via-2.x.y/src/index.html) : defines the user interface components 
like menu bar, toolbar, annotation editor, shape selector, file list, etc.
 * [via.css](via-2.x.y/src/via.css) : describes the style (e.g. colour, font size, 
border, etc.) of user interface components defined in [index.html](via-2.x.y/src/index.html).
 * [via.js](via-2.x.y/src/via.js) : Javascript code that manages user interactions 
(e.g. draw regions, select region shape, etc.) and other aspects of the VIA 
application (e.g. load file, import/export annotations, edit metadata, etc.)

The above three files are combined by [pack_via.py](via-2.x.y/scripts/pack_via.py)
script to generate the final VIA application file named [via.html](via-2.x.y/dist/via.html).

More details about the VIA source code is available in the [source code documentation](via-2.x.y/CodeDoc.md)
file. All the files related to the VIA application reside in the [via-2.x.y branch](https://gitlab.com/vgg/via/tree/via-2.x.y/via-2.x.y)
of the source code repository. The [Quality Assessment](via-2.x.y/QualityAssessment.md) 
page describes the guidelines to ensure the quality of VIA application, source 
code and its documentation.

Software bug reports and feature requests should be 
[submitted here](https://gitlab.com/vgg/via/issues/new) (requires gitlab account).

## License
VIA is an open source project released under the 
[BSD-2 clause license](https://gitlab.com/vgg/via/blob/master/LICENSE).

## Contact
Contact [Abhishek Dutta](adutta_remove_me_@robots.ox.ac.uk) for any queries or feedback related to this application.

## Acknowledgements
This work is supported by EPSRC programme grant Seebibyte: Visual Search for the Era of Big Data ( [EP/M013774/1](http://www.seebibyte.org/index.html) )

