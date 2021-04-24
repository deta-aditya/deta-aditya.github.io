import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../app_styling.dart';
import 'primary_button.dart';

class HeroSection extends StatelessWidget {
  const HeroSection({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.symmetric(
        horizontal: context.read<AppStyling>().horizontalPagePadding,
        vertical: context.read<AppStyling>().verticalPagePadding,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "Hello, I'm",
            style: TextStyle(fontSize: 36),
          ),
          Text(
            "Deta Aditya",
            style: TextStyle(
              fontSize: 72,
              fontWeight: FontWeight.w600,
            ),
          ),
          Text(
            "I'm a software developer",
            style: TextStyle(
              fontSize: 36,
              fontWeight: FontWeight.w600,
            ),
          ),
          SizedBox(
            height: 48,
          ),
          PrimaryButton(
            onPressed: () {},
            text: "Contact Me",
          ),
        ],
      ),
    );
  }
}