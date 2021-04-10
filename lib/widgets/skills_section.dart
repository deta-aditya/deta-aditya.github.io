import 'package:flutter/material.dart';

const String description = """
I have been learning web development since 2012 and never stop until this very day. I have used HTML, CSS, and JavaScript many times and fluent with latest JavaScript language specification we often call ES6. JavaScript is also my main language.

I’m looking forward to work on a React or Vue project. I personally prefer working in TypeScript rather than JavaScript, but still open for a JavaScript codebase.
""";

class SkillsSection extends StatelessWidget {
  const SkillsSection({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(
        horizontal: 128.0,
        vertical: 50.0,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "Skills",
            style: TextStyle(
              fontSize: 36,
              fontWeight: FontWeight.w700,
            ),
          ),
          SizedBox(height: 20),
          SkillItem(
            title: "Web Development",
            desc: description,
            code: "print(\"Hello, World!\")",
          ),
        ],
      ),
    );
  }
}

class SkillItem extends StatelessWidget {
  const SkillItem({
    Key key,
    @required this.title,
    @required this.desc,
    @required this.code,
  }) : super(key: key);

  final String title;
  final String desc;
  final String code;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.max,
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(title, style: TextStyle(fontSize: 28)),
            SizedBox(height: 20),
            Container(
              width: 450,
              child: Text(
                description,
                style: TextStyle(fontSize: 18, height: 1.5),
              ),
            ),
          ],
        ),
        Column(
          children: [
            Container(
              width: 500,
              height: 35,
              decoration: BoxDecoration(
                gradient: LinearGradient(
          begin: FractionalOffset.topCenter,
          end: FractionalOffset.bottomCenter,
          colors: <Color>[
            Color(0xFF1E1E1E),
            Color(0xFF000000),
          ],
        ),
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(10),
                  topRight: Radius.circular(10),
                ),
              ),
            ),
            Container(
              width: 500,
              height: 300,
              padding: const EdgeInsets.all(20.0),
              decoration: BoxDecoration(
              color: Color(0xFF202020),
                borderRadius: BorderRadius.only(
                  bottomLeft: Radius.circular(10),
                  bottomRight: Radius.circular(10),
                ),
              ),
              child: Text(
                code,
                style: TextStyle(
                  color: Colors.white,
                ),
              ),
            ),
          ],
        )
      ],
    );
  }
}
