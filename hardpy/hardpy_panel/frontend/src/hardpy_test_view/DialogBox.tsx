import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import {
  Button,
  Classes,
  Dialog,
  InputGroup,
  Radio,
  Checkbox,
  Tab,
  Tabs,
} from "@blueprintjs/core";
import { notification } from "antd";

interface Props {
  title_bar: string;
  dialog_text: string;
  onConfirm?: (inputText: string) => void;
  widget_type?: WidgetType;
  widget_info?: WidgetInfo;
  image_base64?: string;
  image_width?: number;
  image_border?: number;
  is_visible?: boolean;
  id?: string;
  font_size?: number;
  html_url?: string;
  html_code?: string;
  html_width?: number;
  html_border?: number;
}

export enum WidgetType {
  Base = "base",
  TextInput = "textinput",
  NumericInput = "numericinput",
  RadioButton = "radiobutton",
  Checkbox = "checkbox",
  Multistep = "multistep",
}

interface ImageComponent {
  base64?: string;
  width?: number;
  border?: number;
}

interface HTMLComponent {
  code_or_url?: string;
  is_raw_html?: boolean;
  width?: number;
  border?: number;
}

interface StepWidgetInfo {
  type: string;
  info: WidgetInfo;
}

interface StepInfo {
  title: string;
  text?: string;
  widget?: StepWidgetInfo;
  image?: ImageComponent;
  html?: HTMLComponent;
}

interface Step {
  type: string;
  info: StepInfo;
}

interface WidgetInfo {
  fields?: string[];
  text?: string;
  steps?: Step[];
}

interface TextInputComponentProps {
  inputText: string;
  setInputText: (value: string) => void;
  handleKeyDown: (event: React.KeyboardEvent) => void;
  inputPlaceholder: string;
  type: string;
}

interface RadioButtonComponentProps {
  fields: string[];
  selectedRadioButton: string;
  setSelectedRadioButton: (value: string) => void;
  handleKeyDown: (event: React.KeyboardEvent) => void;
  fontSize: number;
}

interface CheckboxComponentProps {
  fields: string[];
  selectedCheckboxes: string[];
  setSelectedCheckboxes: (value: string[]) => void;
  handleKeyDown: (event: React.KeyboardEvent) => void;
  fontSize: number;
}

/**
 * TextInputComponent is a reusable input component that allows users to enter text.
 * @param {string} inputText - The current value of the input field.
 * @returns {JSX.Element} - A controlled input component with auto-focus enabled.
 */
const TextInputComponent = ({
  inputText,
  setInputText,
  handleKeyDown,
  inputPlaceholder,
  type,
}: TextInputComponentProps): JSX.Element => (
  <InputGroup
    value={inputText}
    onChange={(event: React.ChangeEvent<HTMLInputElement>) =>
      setInputText(event.target.value)
    }
    onKeyDown={handleKeyDown}
    placeholder={inputPlaceholder}
    type={type}
    autoFocus={true}
  />
);

/**
 * RadioButtonComponent is a reusable component that renders a group of radio buttons.
 * @param {string[]} fields - An array of options to display as radio buttons.
 * @param {function} setSelectedRadioButton - A function to update the selected radio button.
 * @param {function} handleKeyDown - A function to handle keydown events on the radio buttons.
 * @param {number} fontSize - The font size for the radio button labels.
 * @returns {JSX.Element} - A group of radio buttons with dynamic styling and auto-focus on the first option.
 */
/** */
const RadioButtonComponent = ({
  fields,
  selectedRadioButton,
  setSelectedRadioButton,
  handleKeyDown,
  fontSize,
}: RadioButtonComponentProps): JSX.Element => (
  <>
    {fields?.map((option: string) => (
      <Radio
        key={option}
        label={option}
        checked={selectedRadioButton === option}
        onChange={() => setSelectedRadioButton(option)}
        onKeyDown={handleKeyDown}
        style={{ fontSize: `${fontSize}px` }}
        autoFocus={option === fields[0]}
      />
    ))}
  </>
);

/**
 * CheckboxComponent is a reusable component that renders a group of checkboxes.
 *
 * @param {string[]} fields - An array of options to display as checkboxes.
 * @param {string[]} selectedCheckboxes - An array of currently selected checkbox values.
 * @param {function} setSelectedCheckboxes - A function to update the selected checkboxes.
 * @param {function} handleKeyDown - A function to handle keydown events on the checkboxes.
 * @param {number} fontSize - The font size for the checkbox labels.
 * @returns {JSX.Element} - A group of checkboxes with dynamic styling and auto-focus on the first option.
 */
/** */
const CheckboxComponent = ({
  fields,
  selectedCheckboxes,
  setSelectedCheckboxes,
  handleKeyDown,
  fontSize,
}: CheckboxComponentProps): JSX.Element => (
  <>
    {fields?.map((option: string) => (
      <Checkbox
        key={option}
        label={option}
        checked={selectedCheckboxes.includes(option)}
        autoFocus={option === fields[0]}
        onKeyDown={handleKeyDown}
        style={{ fontSize: `${fontSize}px` }}
        onChange={() => {
          if (selectedCheckboxes.includes(option)) {
            setSelectedCheckboxes(
              selectedCheckboxes.filter((item) => item !== option)
            );
          } else {
            setSelectedCheckboxes([...selectedCheckboxes, option]);
          }
        }}
      />
    ))}
  </>
);

/**
 * Renders a text input component.
 * @param {Props} props - The properties passed to the component.
 * @param {string} inputText - The current value of the input field.
 * @param {function} setInputText - A function to update the value of the input field.
 * @param {function} handleKeyDown - A function to handle keydown events on the input field.
 * @returns {JSX.Element} - A text input component with specified properties.
 */
const renderTextInput = (
  props: Props,
  inputText: string,
  setInputText: (value: string) => void,
  handleKeyDown: (event: React.KeyboardEvent) => void
): JSX.Element => (
  <TextInputComponent
    inputText={inputText}
    setInputText={setInputText}
    handleKeyDown={handleKeyDown}
    inputPlaceholder="enter answer"
    type="text"
  />
);

/**
 * Renders a numeric input component.
 * @param {Props} props - The properties passed to the component.
 * @param {string} inputText - The current value of the input field.
 * @param {function} setInputText - A function to update the value of the input field.
 * @param {function} handleKeyDown - A function to handle keydown events on the input field.
 * @returns {JSX.Element} - A numeric input component with specified properties.
 */
const renderNumericInput = (
  props: Props,
  inputText: string,
  setInputText: (value: string) => void,
  handleKeyDown: (event: React.KeyboardEvent) => void
): JSX.Element => (
  <TextInputComponent
    inputText={inputText}
    setInputText={setInputText}
    handleKeyDown={handleKeyDown}
    inputPlaceholder="enter answer"
    type="number"
  />
);

/**
 * Renders a radio button component.
 * @param {Props} props - The properties passed to the component.
 * @param {string} selectedRadioButton - The currently selected radio button.
 * @param {function} setSelectedRadioButton - A function to update the selected radio button.
 * @param {function} handleKeyDown - A function to handle keydown events on the radio buttons.
 * @returns {JSX.Element} - A radio button component with specified properties.
 */
const renderRadioButton = (
  props: Props,
  selectedRadioButton: string,
  setSelectedRadioButton: (value: string) => void,
  handleKeyDown: (event: React.KeyboardEvent) => void
): JSX.Element => (
  <RadioButtonComponent
    fields={props.widget_info?.fields ?? []}
    selectedRadioButton={selectedRadioButton}
    setSelectedRadioButton={setSelectedRadioButton}
    handleKeyDown={handleKeyDown}
    fontSize={props.font_size ?? 12}
  />
);

/**
 * Renders a checkbox component.
 * @param {Props} props - The properties passed to the component.
 * @param {string[]} selectedCheckboxes - An array of currently selected checkbox values.
 * @param {function} setSelectedCheckboxes - A function to update the selected checkboxes.
 * @param {function} handleKeyDown - A function to handle keydown events on the checkboxes.
 * @returns {JSX.Element} - A checkbox component with specified properties.
 */
const renderCheckbox = (
  props: Props,
  selectedCheckboxes: string[],
  setSelectedCheckboxes: (value: string[]) => void,
  handleKeyDown: (event: React.KeyboardEvent) => void
): JSX.Element => (
  <CheckboxComponent
    fields={props.widget_info?.fields ?? []}
    selectedCheckboxes={selectedCheckboxes}
    setSelectedCheckboxes={setSelectedCheckboxes}
    handleKeyDown={handleKeyDown}
    fontSize={props.font_size ?? 12}
  />
);


/**
 * Renders an HTML code iframe.
 * @param {string} htmlCode - The HTML code to render.
 * @param {number} height - The height of the iframe.
 * @param {number} width - The width of the iframe.
 * @param {number} border - The border size of the iframe.
 * @returns {JSX.Element} - An iframe element with the specified HTML code.
 */
/** */
const renderHTMLCode = (
  htmlCode: string,
  width: number,
  border: number
): JSX.Element => (
  <iframe
    srcDoc={htmlCode}
    width={`${width}%`}
    style={{
      border: `${border}px solid black`,
      height: "auto",
      minHeight: "300px",
    }}
    title="HTML Code"
  />
);

/**
 * Renders an HTML link iframe.
 * @param {string} htmlUrl - The URL to render.
 * @param {number} height - The height of the iframe.
 * @param {number} width - The width of the iframe.
 * @param {number} border - The border size of the iframe.
 * @returns {JSX.Element} - An iframe element with the specified URL.
 */
/** */
const renderHTMLLink = (
  htmlUrl: string,
  width: number,
  border: number
): JSX.Element => (
  <iframe
    src={htmlUrl}
    width={`${width}%`}
    style={{
      border: `${border}px solid black`,
      height: "auto",
      minHeight: "300px",
    }}
    title="HTML Link"
  />
);

/**
 * Renders a multistep component with tabs, each containing text, images, or HTML content.
 * @param {Props} props - The properties passed to the component.
 * @param {Object} imageStepDimensions - The dimensions of the image step.
 * @param {Object} baseDialogDimensions - The base dimensions of the dialog.
 * @param {number} htmlHeightIndex - The height index for HTML content.
 * @param {number} htmlWidthIndex - The width index for HTML content.
 * @param {React.CSSProperties} imageStyle - The style properties for the image.
 * @returns {JSX.Element} - A multistep component with tabs containing various content types.
 */
/** */
const renderMultistep = (
  props: Props,
  imageStyle: React.CSSProperties
): JSX.Element => (
  <Tabs id={props.title_bar}>
    {props.widget_info?.steps?.map((step: Step) => (
      <Tab
        id={step.info?.title}
        key={step.info?.title}
        title={step.info?.title}
        style={{ fontSize: `${props.font_size}px` }}
        panel={
          <div className="step-container">
            <div className="step-content">
              {step.info?.text?.split("\n").map((line) => (
                <p key={line} style={{ textAlign: "left" }}>
                  {line}
                </p>
              ))}
              {step.info.image && (
                <img
                  src={`data:image/image;base64,${step.info.image?.base64}`}
                  alt={""}
                  style={{
                    width: `${step.info.image?.width ?? 100}%`,
                    maxWidth: '100%',
                    height: "auto",
                    objectFit: 'contain',
                    ...imageStyle,
                  }}
                />
              )}
              {step.info.html?.code_or_url &&
                step.info.html?.is_raw_html &&
                renderHTMLCode(
                  step.info.html.code_or_url,
                  step.info.html?.width ?? 100,
                  step.info.html?.border ?? 0
                )}
              {step.info.html?.code_or_url &&
                !step.info.html?.is_raw_html &&
                renderHTMLLink(
                  step.info.html.code_or_url,
                  step.info.html?.width ?? 100,
                  step.info.html?.border ?? 0
                )}
            </div>
          </div>
        }
      ></Tab>
    ))}
  </Tabs>
);

/**
 * StartConfirmationDialog is a React component that renders a dialog box with various types of input widgets.
 * It supports text input, numeric input, radio buttons, checkboxes, and multi-step forms.
 *
 * @param {Props} props - The properties passed to the component.
 * @returns {JSX.Element} - The rendered dialog box.
 */
export function StartConfirmationDialog(props: Readonly<Props>): JSX.Element {
  const [dialogOpen, setDialogOpen] = useState(false);
  const [inputText, setInputText] = useState("");
  const [selectedRadioButton, setSelectedRadioButton] = useState("");
  const [selectedCheckboxes, setSelectedCheckboxes] = useState<string[]>([]);
  const [dialogDimensions, setDialogDimensions] = useState({
    width: "auto",
    height: "auto",
    maxHeight: "90vh",
  });
  const dialogRef = useRef<HTMLDivElement>(null);
  const widgetType = props.widget_type ?? WidgetType.Base;
  const [maxContentDimensions, setMaxContentDimensions] = useState({
    width: 0,
    height: 0,
  });

  useEffect(() => {
    if (widgetType === WidgetType.Multistep && props.widget_info?.steps) {
      const tempContainer = document.createElement("div");
      tempContainer.style.visibility = "hidden";
      tempContainer.style.position = "absolute";
      tempContainer.style.width = "400px";
      document.body.appendChild(tempContainer);
  
      let maxWidth = 0;
      let maxHeight = 0;
      let pendingLoads = 0;
  
      const checkAllLoaded = () => {
        if (pendingLoads === 0) {
          document.body.removeChild(tempContainer);
          setMaxContentDimensions({ width: maxWidth, height: maxHeight });
        }
      };
  
      props.widget_info.steps.forEach((step) => {
        const stepContent = document.createElement("div");
        stepContent.className = "step-content";
        stepContent.style.padding = "10px";

        if (step.info?.text) {
          const textElement = document.createElement("div");
          textElement.innerHTML = step.info.text.split("\n").join("<br/>");
          stepContent.appendChild(textElement);
        }

        if (step.info?.image) {
          pendingLoads++;
          const img = new Image();
          img.onload = () => {
            const rect = stepContent.getBoundingClientRect();
            maxWidth = Math.max(maxWidth, rect.width);
            maxHeight = Math.max(maxHeight, rect.height);
            pendingLoads--;
            checkAllLoaded();
          };
          img.src = `data:image/image;base64,${step.info.image.base64}`;
          img.style.width = `${step.info.image.width ?? 100}%`;
          img.style.maxWidth = "100%";
          img.style.height = "auto";
          stepContent.appendChild(img);
        }

        if (step.info?.html && !step.info.html.is_raw_html) {
          pendingLoads++;
          const iframe = document.createElement("iframe");
          iframe.onload = () => {
            setTimeout(() => {
              const rect = stepContent.getBoundingClientRect();
              maxWidth = Math.max(maxWidth, rect.width);
              maxHeight = Math.max(maxHeight, rect.height);
              pendingLoads--;
              checkAllLoaded();
            }, 300);
          };
          iframe.src = step.info.html.code_or_url ?? "";
          iframe.width = `${step.info.html.width ?? 100}%`;
          iframe.style.border = "none";
          stepContent.appendChild(iframe);
        }
  
        tempContainer.appendChild(stepContent);
        
        if (!step.info?.image && (!step.info?.html || step.info.html.is_raw_html)) {
          const rect = stepContent.getBoundingClientRect();
          maxWidth = Math.max(maxWidth, rect.width);
          maxHeight = Math.max(maxHeight, rect.height);
        }
      });
  
      checkAllLoaded();
    }
  }, [props.widget_info?.steps, widgetType]);


  useEffect(() => {
    if (widgetType === WidgetType.Multistep && dialogOpen) {
      const handleTabChange = () => {
        setTimeout(calculateDialogSize, 100);
      };
  
      const tabs = dialogRef.current?.querySelector(".bp4-tab-list");
      if (tabs) {
        tabs.addEventListener("click", handleTabChange);
      }
  
      return () => {
        if (tabs) {
          tabs.removeEventListener("click", handleTabChange);
        }
      };
    }
  }, [widgetType, dialogOpen]);

  const calculateDialogSize = () => {
    if (!dialogRef.current) {
      return;
    }

    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;
    const maxWidth = windowWidth * 0.9;
    const maxHeight = windowHeight * 0.9;

    let contentWidth = 400;
    let contentHeight = 300;

    if (widgetType === WidgetType.Multistep) {
      contentWidth = Math.min(
        Math.max(maxContentDimensions.width + 40, 400),
        maxWidth
      );
      contentHeight = Math.min(
        Math.max(maxContentDimensions.height + 100, 300),
        maxHeight
      );
    } else {
      const contentElement = dialogRef.current.querySelector(
        `.${Classes.DIALOG_BODY}`
      );
      if (contentElement) {
        contentWidth = Math.min(contentElement.scrollWidth + 40, maxWidth);
        contentHeight = Math.min(contentElement.scrollHeight + 100, maxHeight);
      }
    }

    setDialogDimensions({
      width: `${contentWidth}px`,
      height: `${contentHeight}px`,
      maxHeight: `${maxHeight}px`,
    });
  };

  const handleClose = () => {
    setDialogOpen(false);
    fetch("api/stop")
      .then((response) => {
        if (response.ok) {
          return response.text();
        } else {
          console.log("Request failed. Status: " + response.status);
        }
      })
      .catch((error) => {
        console.log("Request failed. Error: " + error);
      });
    notification.error({
      message: "Notification",
      description: "The window was closed. Tests stopped.",
    });
  };

  /**
   * Handles the confirm event of the dialog box.
   * Validates the input and sends the confirmed data to the server.
   */
  const handleConfirm = async () => {
    if (props.widget_type) {
      switch (props.widget_type) {
        case WidgetType.TextInput:
        case WidgetType.NumericInput:
          if (
            inputText.trim() === "" ||
            inputText === "." ||
            inputText === ".."
          ) {
            alert("The field must not be empty");
            return;
          }
          break;
        case WidgetType.RadioButton:
          if (selectedRadioButton === "") {
            alert("The field must not be empty");
            return;
          }
          break;
        case WidgetType.Checkbox:
          if (selectedCheckboxes.length === 0) {
            alert("The field must not be empty");
            return;
          }
          break;
        default:
          break;
      }
    }
    setDialogOpen(false);
    let textToSend = "";

    /**
     * Encodes a URL component, replacing special characters with their hexadecimal equivalents.
     *
     * @param {string} str - The string to encode.
     * @returns {string} - The encoded string.
     */
    function processEncodeURLComponent(str: string): string {
      return encodeURIComponent(str).replace(
        /[!-'()*+,/:;<=>?@[\]^`{|}~]/g,
        function (c) {
          return "%" + c.charCodeAt(0).toString(16);
        }
      );
    }

    switch (props.widget_type) {
      case WidgetType.TextInput:
        textToSend = processEncodeURLComponent(inputText);
        break;
      case WidgetType.NumericInput:
        textToSend = inputText;
        break;
      case WidgetType.RadioButton:
        textToSend = processEncodeURLComponent(selectedRadioButton);
        break;
      case WidgetType.Checkbox:
        textToSend = JSON.stringify(
          selectedCheckboxes.map((checkboxValue) =>
            processEncodeURLComponent(checkboxValue)
          )
        );
        break;
      default:
        textToSend = "ok";
        break;
    }

    if (props.onConfirm) {
      props.onConfirm(textToSend);
    }
    try {
      const response = await axios.post(
        `/api/confirm_dialog_box/${textToSend}`
      );
      console.log(response.data);
    } catch (error) {
      console.error("Error confirming dialog box:", error);
    }
  };

  /**
   * Handles keydown events for the dialog box.
   *
   * @param {React.KeyboardEvent} event - The keyboard event.
   */
  const handleKeyDown = (event: React.KeyboardEvent) => {
    const key = event.key;

    if (key === "Enter") {
      handleConfirm();
      return;
    }

    if (props.widget_info?.fields) {
      handleWidgetKeyDown(key);
    }
  };

  /**
   * Handles keydown events for widget-specific actions.
   *
   * @param {string} key - The key that was pressed.
   */
  const handleWidgetKeyDown = (key: string) => {
    const index =
      props.widget_info?.fields?.findIndex((option) =>
        option.startsWith(key)
      ) ?? -1;

    if (index >= 0) {
      if (widgetType === WidgetType.RadioButton) {
        if (props.widget_info?.fields) {
          setSelectedRadioButton(props.widget_info.fields[index]);
        }
      } else if (widgetType === WidgetType.Checkbox) {
        if (props.widget_info?.fields) {
          const option = props.widget_info.fields[index];
          if (selectedCheckboxes.includes(option)) {
            setSelectedCheckboxes(
              selectedCheckboxes.filter((item) => item !== option)
            );
          } else {
            setSelectedCheckboxes([...selectedCheckboxes, option]);
          }
        }
      }
    }
  };

  useEffect(() => {
    if (dialogOpen) {
      setTimeout(calculateDialogSize, 50);

      window.addEventListener("resize", calculateDialogSize);
      return () => window.removeEventListener("resize", calculateDialogSize);
    }
  }, []);

  type ObjectFit = "contain" | "cover" | "fill" | "none" | "scale-down";

  const imageStyle = {
    border: `${props.image_border ?? 0}px solid black`,
    display: "block",
    margin: "0 auto",
    maxWidth: "100%",
    width:
      widgetType === WidgetType.Multistep
        ? "auto"
        : `${props.image_width ?? 100}%`,
    height: "auto",
    objectFit: "contain" as ObjectFit, // Use the as keyword to assert the type
  };

  useEffect(() => {
    if (props.is_visible) {
      setDialogOpen(true);
    }
  }, [props.is_visible, props.id]);

  return (
    <Dialog
      title={props.title_bar}
      icon="info-sign"
      isOpen={dialogOpen}
      onClose={handleClose}
      canOutsideClickClose={false}
      style={{
        width: dialogDimensions.width,
        height: dialogDimensions.height,
        maxHeight: dialogDimensions.maxHeight,
        minWidth: "400px",
        minHeight: "300px",
        fontSize: `${props.font_size}px`,
      }}
    >
      <div
        className={Classes.DIALOG_BODY}
        style={{
          wordWrap: "break-word",
          wordBreak: "break-word",
          overflowY: "auto",
          padding: "10px",
          maxHeight: `calc(${dialogDimensions.maxHeight} - 100px)`,
        }}
      >
        {props.dialog_text.split("\n").map((line) => (
          <p key={line.trim()} style={{ textAlign: "left" }}>
            {line}
          </p>
        ))}
        {widgetType === WidgetType.TextInput &&
          renderTextInput(props, inputText, setInputText, handleKeyDown)}
        {widgetType === WidgetType.NumericInput &&
          renderNumericInput(props, inputText, setInputText, handleKeyDown)}
        {widgetType === WidgetType.RadioButton &&
          renderRadioButton(
            props,
            selectedRadioButton,
            setSelectedRadioButton,
            handleKeyDown
          )}
        {widgetType === WidgetType.Checkbox &&
          renderCheckbox(
            props,
            selectedCheckboxes,
            setSelectedCheckboxes,
            handleKeyDown
          )}
        {widgetType === WidgetType.Multistep &&
          renderMultistep(props, imageStyle)}
        <p> </p>
        {props.image_base64 && (
          <div className="image-container">
            <img
              src={`data:image/image;base64,${props.image_base64}`}
              alt={""}
              style={{ ...imageStyle, height: "auto" }}
            />
          </div>
        )}
        {props.html_code &&
          renderHTMLCode(
            props.html_code,
            props.html_width ?? 100,
            props.html_border ?? 0
          )}
        {props.html_url &&
          renderHTMLLink(
            props.html_url,
            props.html_width ?? 100,
            props.html_border ?? 0
          )}
      </div>
      <div className={Classes.DIALOG_FOOTER}>
        <Button
          intent="primary"
          onClick={handleConfirm}
          autoFocus={
            widgetType === WidgetType.Base ||
            widgetType === WidgetType.Multistep
          }
        >
          Confirm
        </Button>
      </div>
    </Dialog>
  );
}

export default StartConfirmationDialog;
