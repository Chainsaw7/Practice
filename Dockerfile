FROM openjdk:8
COPY . tutorial
WORKDIR tutorial
RUN javac Puppy.java
CMD ["java" , "Puppy"]