import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:web_profile/app_styling.dart';

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
    final appStyling = context.read<AppStyling>();

    return Padding(
      padding: EdgeInsets.only(
        top: appStyling.sizeBetweenSections,
        right: appStyling.horizontalPagePadding,
        bottom: appStyling.sizeBetweenSections,
        left: appStyling.horizontalPageDiscountPadding,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: EdgeInsets.only(left: appStyling.discountedHorizontalPagePadding),
            child: Text(
              "Skills",
              style: TextStyle(
                fontSize: 36,
                fontWeight: FontWeight.w700,
              ),
            ),
          ),
          SizedBox(height: 20),
          SkillItem(
            title: "Web Development",
            desc: description,
            code: RichText(
              text: TextSpan(
                style: TextStyle(color: Colors.white),
                children: <TextSpan>[
                  TextSpan(
                    text: 'import',
                    style: TextStyle(color: appStyling.codeKeywordColor),
                  ),
                  TextSpan(text: ' React '),
                  TextSpan(
                    text: 'from',
                    style: TextStyle(color: appStyling.codeKeywordColor),
                  ),
                  TextSpan(
                    text: " 'react'",
                    style: TextStyle(color: appStyling.codeStringColor),
                  ),
                  TextSpan(text: "\nFoo"),
                ],
              ),
            ),
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
  final Widget code;

  @override
  Widget build(BuildContext context) {
    final appStyling = context.read<AppStyling>();

    return Row(
      mainAxisSize: MainAxisSize.max,
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Padding(
                  padding: EdgeInsets.symmetric(
                    horizontal: appStyling.discountedHorizontalMarkerPadding,
                  ),
                  child: Container(
                    height: appStyling.markerSize,
                    width: appStyling.markerSize,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(appStyling.markerSize),
                      color: Color(0xFFC4C4C4),
                    ),
                  ),
                ),
                Text(title, style: TextStyle(fontSize: 28)),
              ],
            ),
            SizedBox(height: 20),
            Row(
              children: [
                SizedBox(width: appStyling.discountedHorizontalPagePadding),
                Container(
                  width: 450,
                  child: Text(
                    description,
                    style: TextStyle(fontSize: 18, height: 1.5),
                  ),
                ),
              ],
            ),
          ],
        ),
        Column(
          children: [
            Container(
              width: appStyling.codeWindowWidth,
              height: appStyling.codeWindowFrameHeight,
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
              width: appStyling.codeWindowWidth,
              height: 300,
              padding: const EdgeInsets.all(20.0),
              decoration: BoxDecoration(
                color: Color(0xFF202020),
                borderRadius: BorderRadius.only(
                  bottomLeft: Radius.circular(10),
                  bottomRight: Radius.circular(10),
                ),
              ),
              child: code,
            ),
          ],
        )
      ],
    );
  }
}
